import uuid

class Claim:
    def __init__(self, date, incident_description, claim_amount, customer_id, approved_amount, agent_id):
        self.ID = str(uuid.uuid1())
        self.date = date
        self.incident_description = incident_description
        self.claim_amount = claim_amount
        self.customer_id = customer_id
        self.approved_amount = approved_amount
        self.agent_id = agent_id

    def serialize(self):
        return {
            'id': self.ID,
            'date': self.date,
            'incident_description': self.incident_description,
            'claim_amount': self.claim_amount,
            'customer_id': self.customer_id,
            'approved_amount': self.approved_amount,
            'agent_id': self.agent_id
        }

