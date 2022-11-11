
class Bill:
    """
    Contains information of the bill such as amount and time period
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate who will be paying the share of bill
    """

    def __init__(self, name, days_stayed):
        self.name = name
        self.days_stayed = days_stayed

    def pays(self, bill, shared_flatmate):
        weight = self.days_stayed / (self.days_stayed + shared_flatmate.days_stayed)
        to_pay = bill.amount * weight
        return to_pay

