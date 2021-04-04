from flask import Flask, request, jsonify
from InsuranceCompany import *
from Customer import *
from collections import OrderedDict

app = Flask(__name__)

# Root object for the insurance company
company = InsuranceCompany("Be-Safe Insurance Company")


# Predefined data.
@app.route("/predefined", methods=['POST'])
def Predefined():
    cid = company.addCustomer('Nevi', 'Vienna')
    cid2 = company.addCustomer('Marti', 'London')
    cid3 = company.addCustomer('Geri', 'Edinburgh')
    cid4 = company.addCustomer("Majdramunqk", "Pri mamina zlatna")
    aid = company.addAgent('Gencho', 'Vienna')
    aid2 = company.addAgent('Krisi', 'Sofia')
    aid3 = company.addAgent('Naliya', 'New York')
    a = company.getAgentById(aid)
    a2 = company.getAgentById(aid2)
    a3 = company.getAgentById(aid3)
    c = company.getCustomerById(cid)
    c2 = company.getCustomerById(cid2)
    c3 = company.getCustomerById(cid3)
    c4 = company.getCustomerById(cid4)
    if (a != None):
        if (c != None):
            a.addCustomer(c)
            c.addAgentID(aid)
    if (a2 != None):
        if (c2 != None):
            a2.addCustomer(c2)
            c2.addAgentID(aid2)
        if (c3 != None):
            a2.addCustomer(c3)
            c3.addAgentID(aid2)
    clid1 = company.addClaim('31-03-20', 'Dobro', '23', cid, 'PARTLY COVERED', aid)
    clid2 = company.addClaim('21-02-19', 'Losho', '7382', cid, 'COVERED', aid)
    clid3 = company.addClaim('31-03-21', 'Stava', '23', cid2, 'PARTLY COVERED', aid2)
    clid4 = company.addClaim('12-12-20', 'Nishto osobeno', '7382', cid2, 'COVERED', aid2)
    c.addClaim(company.getClaimById(clid1))
    c.addClaim(company.getClaimById(clid2))
    c2.addClaim(company.getClaimById(clid3))
    c2.addClaim(company.getClaimById(clid4))
    company.addPaymentOUT('12-02-17', aid, '1234')
    company.addPaymentOUT('23-12-18', aid, '1454')
    company.addPaymentOUT('11-05-19', aid2, '10000')
    company.addPaymentOUT('20-12-18', aid2, '1234')
    company.addPaymentIN('11-05-19', cid, '10000')
    company.addPaymentIN('20-12-18', cid2, '1234')
    company.addPaymentIN('20-12-18', cid3, '1004')
    return jsonify(f"Added predefined data.")


# Add a new customer (parameters: name, address).
@app.route("/customer", methods=["POST"])
def addCustomer():
    # parameters are passed in the body of the request
    cid = company.addCustomer(request.args.get('name'), request.args.get('address'))
    return jsonify(f"Added a new customer with ID {cid}")


# Return the details of a customer of the given customer_id.
@app.route("/customer/<customer_id>", methods=["GET"])
def customerInfo(customer_id):
    c = company.getCustomerById(customer_id)
    if (c != None):
        return jsonify(c.serialize())
    return jsonify(
        success=False,
        message="Customer not found")


# Add a new car (parameters: model, numberplate).
@app.route("/customer/<customer_id>/car", methods=["POST"])
def addCar(customer_id):
    c = company.getCustomerById(customer_id)
    if (c != None):
        car = Car(request.args.get('model_name'), request.args.get('number_plate'), request.args.get('motor_power'), request.args.get('year'))
        c.addCar(car)
        return jsonify(
            success=c != None,
            message=f"Car added to customer with ID {customer_id}")
    return jsonify(
        success=c != None,
        message="Customer not found")


@app.route("/customer/<customer_id>", methods=["DELETE"])
def deleteCustomer(customer_id):
    result = company.deleteCustomer(customer_id)
    if (result):
        message = f"Customer with id{customer_id} was deleted"
    else:
        message = "Customer not found"
    return jsonify(
        success=result,
        message=message)


@app.route("/customers", methods=["GET"])
def allCustomers():
    return jsonify(customers=[h.serialize() for h in company.getCustomers()])


# Add a new agent (parameters: name, address).
@app.route("/agent", methods=["POST"])
def addAgent():
    # parameters are passed in the body of the request
    aid = company.addAgent(request.args.get('name'), request.args.get('address'))
    return jsonify(f"Added a new agent with ID {aid}")


# Return the details of a agent of the given agent_id.
@app.route("/agent/<agent_id>", methods=["GET"])
def agentInfo(agent_id):
    a = company.getAgentById(agent_id)
    if (a != None):
        return jsonify(a.serialize())
    return jsonify(
        success=False,
        message="Agent not found")


# Assign a new customer with the provided customer_id to the agent with agent_id.
@app.route("/agent/<agent_id>/<customer_id>", methods=["POST"])
def addCustomertoAgent(agent_id, customer_id):
    a = company.getAgentById(agent_id)
    c = company.getCustomerById(customer_id)
    if (a != None):
        if (c != None):
            a.addCustomer(c)
            c.addAgentID(agent_id)
            return jsonify(
                success=c != None and a != None,
                message=f"Customer with ID {customer_id} added to agent with ID {agent_id}")
    return jsonify(
        success=c != None and a != None,
        message="Customer or agent not found")


# Delete the agent with the given agent_id. And move the customers to other agent first.!!!!!!!!!!!!!!!
@app.route("/agent/<agent_id>", methods=["DELETE"])
def deleteAgent(agent_id):
    a = company.getAgentById(agent_id)
    if (a != None):
        customers = company.getCustomersByAgentID(agent_id)  # get agent customers
        # customers = a.get("customers")
    result = company.deleteAgent(agent_id)
    if (result):
        message = f"Agent with id{agent_id} was deleted"
        # get another agent and assign the other customers to him
        agent = company.getAgent()
        for c in customers:
            agent.addCustomer(c)
    else:
        message = "Agent not found"

    return jsonify(
        success=result,
        message=message)


# Return a list of all agents.
@app.route("/agents", methods=["GET"])
def allAgents():
    return jsonify(agents=[h.serialize() for h in company.getAgents()])


# Add a new insurance claim (parameters: date, incident_description, claim_amount).
@app.route("/claims/<customer_id>/file", methods=["POST"])
def addClaim(customer_id):
    # parameters are passed in the body of the request
    c = company.getCustomerById(customer_id)
    clid = company.addClaim(request.args.get('date'), request.args.get('incident_description'), request.args.get('claim_amount'), customer_id, None, c.agent_id)
    cl = company.getClaimById(clid)
    c.addClaim(cl)
    return jsonify(f"Added a new claim with ID {clid} to customer with ID {customer_id}")


# Return details about the claim with the given claim_id.
@app.route("/claims/<claim_id>", methods=["GET"])
def claimInfo(claim_id):
    cl = company.getClaimById(claim_id)
    if (cl != None):
        return jsonify(cl.serialize())
    return jsonify(
        success=False,
        message="Claim not found")


# Change the status of a claim to REJECTED, PARTLY COVERED or FULLY COVERED. Parameters: approved_amount.
@app.route("/claims/<claim_id>/status", methods=["PUT"])
def claimStatus(claim_id):
    cl = company.getClaimById(claim_id)
    c = company.getCustomerById(cl.customer_id)
    a = company.getAgentById(c.agent_id)
    if (cl != None and a != None):
        status = request.args.get('approved_amount')
        cl.approved_amount = status
        cl.agent_id = a.ID
        return jsonify(f"Added a status to claim with ID {claim_id}")
    return jsonify(
        success=False,
        message="Claim or agent not found")


# Return a list of all claims.
@app.route("/claims", methods=["GET"])
def allClaims():
    return jsonify(claims=[h.serialize() for h in company.getClaims()])


# Add a new payment received from a customer. (parameters: date, customer_id, amount_received)
@app.route("/payment/in/", methods=["POST"])
def addPaymentIN():
    # parameters are passed in the body of the request
    p = company.addPaymentIN(request.args.get('date'), request.args.get('customer_id'), request.args.get('amount_received'))
    c = company.getCustomerById(p.customer_id)
    c.addPayment(p)
    return jsonify(f"Added a new payment received from a customer.")


# Add a new payment transferred to an agent. (parameters: date, agent_id, amount_sent).
@app.route("/payment/out/", methods=["POST"])
def addPaymentOUT():
    # parameters are passed in the body of the request
    p = company.addPaymentOUT(request.args.get('date'), request.args.get('agent_id'), request.args.get('amount_sent'))
    a = company.getAgentById(p.agent_id)
    a.addPayment(p)
    return jsonify(f"Added a new payment transferred to an agent.")


# Return a list of all incoming and outgoing payments.
@app.route("/payments/", methods=["GET"])
def allPayments():
    pin = [h.serialize() for h in company.getPaymentsIn()]
    pout = [h.serialize() for h in company.getPaymentsOut()]
    p = {'in': pin, 'out': pout}
    return jsonify(p)


# Return a list of all claims, grouped by responsible agents.
@app.route("/stats/claims", methods=["GET"])
def allClaimsByAgent():
    claims = [h.serialize() for h in company.getClaims()]
    result = {}
    for cl in claims:
        agent = cl.get("agent_id")
        if (agent != None):
            if agent not in result.keys():
                result[agent] = []
            result[agent].append(cl)

    return jsonify(result)


# Return a list of all revenues, grouped by responsible agents.
@app.route("/stats/revenues", methods=["GET"])
def allRevenuesByAgent():
    payments = [h.serialize() for h in company.getPaymentsOut()]
    result = {}
    for p in payments:
        agent = p.get("agent_id")
        if (agent != None):
            if agent not in result.keys():
                result[agent] = []
            result[agent].append(p)

    return jsonify(result)


# Return a sorted list of agents based on their performance. Be creative and come up with a calculation scheme as performance indicator.
@app.route("/stats/agents", methods=["GET"])
def allAgentsByPreference():
    agents = [h.serialize() for h in company.getAgents()]
    dict_agents = {}
    for a in agents:
        # print(a)
        revenue = company.getRevenueByAgentID(a.get("id"))
        count_c = company.getNumberOfCustomersByAgentID(a.get("id"))
        if (count_c != 0):
            monthly_revenue = revenue/count_c
        else:
            monthly_revenue = 0
        dict_agents[a.get("id")] = monthly_revenue
    print(dict_agents)
    d_descending = sorted(dict_agents, key=dict_agents.get, reverse=True)
    print(d_descending)
    return jsonify(d_descending)


###DO NOT CHANGE CODE BELOW THIS LINE ##############################
@app.route("/")
def index():
    return jsonify(
        success=True,
        message="Your server is running! Welcome to the Insurance Company API.")


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers[
        'Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE"
    return response


if __name__ == "__main__":
    app.run(debug=True, port=8888)
