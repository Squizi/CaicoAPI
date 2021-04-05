import pytest
from Agent import *
from Customer import *
from Payments import *


@pytest.fixture
def data():
    a = Agent('Gencho', 'Vienna')
    c = Customer('Nevi', 'Vienna')
    p = PaymentOutgoing('12-03-21', a.ID, '1900')
    return {'agent': a, 'customer': c, 'paymentout': p}


def test_addCustomer(data):
    a = data.get("agent")
    c = data.get("customer")

    assert c not in a.customers

    a.addCustomer(c)

    assert c in a.customers


def test_addPayment(data):
    a = data.get("agent")
    p = data.get("paymentout")

    assert p not in a.payments

    a.addPayment(p)

    assert p in a.payments
