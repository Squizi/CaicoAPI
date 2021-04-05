import pytest
from Agent import *
from Customer import *
from Payments import *
from Claims import *
from InsuranceCompany import *


@pytest.fixture
def data():
    company = InsuranceCompany("Caico")
    a = Agent('Sarah', 'California')
    company.agents.append(a)
    c = Customer('Leigh', 'New York')
    company.customers.append(c)
    pin = PaymentIncoming('31-03-21', c.ID, '2940')
    company.paymentsin.append(pin)
    pout = PaymentOutgoing('31-03-21', a.ID, '2940')
    company.paymentsout.append(pout)
    car = Car('Zalf', 'SD1234RF', '120', '2000')
    claim = Claim('24-12-19', 'Bad accident', '1234', c.ID, 'PARTLY COVERED', a.ID)
    company.claims.append(claim)
    return {'agent': a, 'customer': c, 'paymentin': pin, 'paymentout': pout, 'car': car, 'claim': claim, 'company': company}


def test_getCustomers(data):
    company = data.get("company")
    # count
    count = len(company.getCustomers())
    assert count == 1


def test_addCustomer(data):
    company = data.get("company")

    company.addCustomer('Lisa', 'Stara Zagora')
    count = len(company.customers)

    assert count == 2


def test_getCustomerById(data):
    company = data.get("company")
    c = data.get("customer")
    customer = company.getCustomerById(c.ID)

    assert customer.name == "Leigh"


def test_deleteCustomer(data):
    company = data.get("company")
    c = data.get("customer")
    cid2 = company.addCustomer('Lisa', 'Stara Zagora')
    count = len(company.customers)

    assert count == 2

    company.deleteCustomer(cid2)
    count = len(company.customers)

    assert count == 1


def test_getAgents(data):
    company = data.get("company")
    count = len(company.getAgents())
    assert count == 1


def test_addAgent(data):
    company = data.get("company")

    company.addAgent('Lisa', 'Stara Zagora')
    count = len(company.agents)

    assert count == 2


def test_getAgentById(data):
    company = data.get("company")
    a = data.get("agent")
    agent = company.getAgentById(a.ID)

    assert agent.name == "Sarah"


def test_deleteAgent(data):
    company = data.get("company")
    a = data.get("agent")
    aid2 = company.addAgent('Lisa', 'Stara Zagora')
    count = len(company.agents)

    assert count == 2

    company.deleteAgent(aid2)
    count = len(company.agents)

    assert count == 1



def test_getClaims(data):
    company = data.get("company")
    count = len(company.getClaims())
    assert count == 1


def test_addClaim(data):
    company = data.get("company")
    cid = company.addCustomer('Lani', 'Str')
    aid = company.addCustomer('Sash', 'Str')

    count = len(company.claims)
    assert count == 1

    company.addClaim('25-07-19', 'incident_description', 'claim_amount', cid, 'COVERED', aid)
    count = len(company.claims)

    assert count == 2


def test_getClaimById(data):
    company = data.get("company")
    cl = data.get("claim")
    claim = company.getClaimById(cl.ID)

    assert claim.date == "24-12-19"


def test_addPaymentIN(data):
    company = data.get("company")
    pin = data.get("paymentin")
    c = data.get("customer")

    count = len(company.paymentsin)
    assert count == 1

    company.addPaymentIN('25-07-19', c.ID, '1234')
    count = len(company.paymentsin)

    assert count == 2


def test_addPaymentOUT(data):
    company = data.get("company")
    pout = data.get("paymentout")
    a = data.get("agent")

    count = len(company.paymentsout)
    assert count == 1

    company.addPaymentOUT('25-07-19', a.ID, '1134')
    count = len(company.paymentsout)

    assert count == 2