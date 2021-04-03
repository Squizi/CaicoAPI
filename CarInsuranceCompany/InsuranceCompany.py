from Customer import *
from Agent import *
from Claims import *
from Payments import *

class InsuranceCompany:
    def __init__(self, name):
        self.name = name  # Name of the Insurance company
        self.customers = []  # list of customers
        self.agents = []  # list of dealers
        self.claims = []  # list of claims
        self.paymentsin = []  # list of incoming payments
        self.paymentsout = []  # list of outgoing payments

        self.addCustomer("majdramunqk", "pri mamina zlatna")


    def getCustomers(self):
        return list(self.customers)

    def addCustomer(self, name, address):
        c = Customer(name, address)
        self.customers.append(c)
        return c.ID

    def getCustomerById(self, id_):
        for d in self.customers:
            if (d.ID == id_):
                return d
        return None

    def deleteCustomer(self, customer_id):
        c = self.getCustomerById(customer_id)
        if (c == None):
            return False
        else:
            self.customers.remove(c)
            return True

    def getAgents(self):
        return list(self.agents)

    def addAgent(self, name, address):
        a = Agent(name, address)
        self.agents.append(a)
        return a.ID

    def getAgentById(self, id_):
        for d in self.agents:
            if (d.ID == id_):
                return d
        return None

    def deleteAgent(self, agent_id):
        a = self.getAgentById(agent_id)
        if (a == None):
            return False
        else:
            self.agents.remove(a)
            return True

    def getClaims(self):
        return list(self.claims)

    def addClaim(self, date, incident_description, claim_amount, customer_id, approved_amount, agent_id):
        cl = Claim(date, incident_description, claim_amount, customer_id, approved_amount, agent_id)
        self.claims.append(cl)
        return cl.ID

    def getClaimById(self, id_):
        for d in self.claims:
            if (d.ID == id_):
                return d
        return None

    def addPaymentIN(self, date, customer_id, amount_received):
        p = PaymentIncoming(date, customer_id, amount_received)
        self.paymentsin.append(p)

    def addPaymentOUT(self, date, agent_id, amount_sent):
        p = PaymentOutgoing(date, agent_id, amount_sent)
        self.paymentsout.append(p)

    def getPaymentsIn(self):
        p = self.paymentsin
        return p

    def getPaymentsOut(self):
        p = self.paymentsout
        return p

