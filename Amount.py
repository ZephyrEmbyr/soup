"""Class amount contains a unit and quantity
for tracking the amount of an ingredient"""
class Amount:

    def __init__(self, quantity, unit):
        self.quantity = quantity
        self.unit = unit

    # setter
    def replace_quantity(self, new_quantity):
        self.quantity = new_quantity

    # getter
    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (str(self.quantity) + " " + str(self.unit))
