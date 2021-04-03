import uuid
from Customer import *
from Payments import *

# Represents the insurance agent
class Agent:
    def __init__(self, name, address):
        self.ID = str(uuid.uuid1())
        self.name = name
        self.address = address
        self.customers = []  # List of customers
        self.payments = []  # List of payments

    def addCustomer(self, customer):
        self.customers.append(customer)

    def addPayment(self, payment):
        self.payments.append(payment)

    # convert object o JSON
    def serialize(self):
        return {
            'id': self.ID,
            'name': self.name,
            'address': self.address,
            'customers': [customer.serialize() for customer in self.customers],
        }
