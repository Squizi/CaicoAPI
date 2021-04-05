import pytest
from Agent import *
from Customer import *
from Payments import *
from Claims import *


@pytest.fixture
def data():
    a = Agent('Sarah', 'California')
    c = Customer('Leigh', 'New York')
    p = PaymentIncoming('31-03-21', c.ID, '2940')
    car = Car('Zalf', 'SD1234RF', '120', '2000')
    claim = Claim('24-12-19', 'Bad accident', '1234', c.ID, 'PARTLY COVERED', a.ID)
    return {'agent': a, 'customer': c, 'paymentin': p, 'car': car, 'claim': claim}


def test_addCar(data):
    car = data.get("car")
    c = data.get("customer")

    assert car not in c.cars

    c.addCar(car)

    assert car in c.cars


def test_addClaim(data):
    claim = data.get("claim")
    c = data.get("customer")

    assert claim not in c.claims

    c.addClaim(claim)

    assert claim in c.claims


def test_addAgentID(data):
    a = data.get("agent")
    c = data.get("customer")

    assert c.agent_id != a.ID

    c.addAgentID(a.ID)

    assert c.agent_id == a.ID


def test_addPayment(data):
    p = data.get("paymentin")
    c = data.get("customer")

    assert p not in c.payments

    c.addPayment(p)

    assert p in c.payments