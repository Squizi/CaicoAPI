class PaymentIncoming:
    def __init__(self, date, customer_id, amount_received):
        self.date = date
        self.customer_id = customer_id
        self.amount_received = amount_received

    # convert object o JSON
    def serialize(self):
        return {
            'date': self.date,
            'customer_id': self.customer_id,
            'amount_received': self.amount_received,
        }


class PaymentOutgoing:
    def __init__(self, date, agent_id, amount_sent):
        self.date = date
        self.agent_id = agent_id
        self.amount_sent = amount_sent

    # convert object o JSON
    def serialize(self):
        return {
            'date': self.date,
            'agent_id': self.agent_id,
            'amount_sent': self.amount_sent,
        }

