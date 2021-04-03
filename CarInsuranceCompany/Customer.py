import uuid
from Agent import *
from Claims import *
from Payments import *

# Represents the customer of the car insurance company
class Customer:
    def __init__(self, name, address):
        self.ID = str(uuid.uuid1())
        self.name = name
        self.address = address
        self.cars = []  # List of cars
        self.claims = []  # List of claims
        self.agent_id = None
        self.payments = []  # List of payments

    def addCar(self, car):
        self.cars.append(car)

    def addClaim(self, claim):
        self.claims.append(claim)

    def addAgentID(self, agent_id):
        self.agent_id = agent_id

    def addPayment(self, payment):
        self.payments.append(payment)

    # convert object o JSON
    def serialize(self):
        return {
            'id': self.ID,
            'name': self.name,
            'address': self.address,
            'cars': [car.serialize() for car in self.cars],
            'claims': [claim.serialize() for claim in self.claims],
            'agent_id': self.agent_id,
        }


class Car:
    def __init__(self, model_name, number_plate, motor_power, year):
        self.model_name = model_name
        self.number_plate = number_plate
        self.motor_power = motor_power
        self.year = year

    def serialize(self):
        return {
            'model_name': self.model_name,
            'number_plate': self.number_plate,
            'motor_power': self.motor_power,
            'year': self.year,
        }


