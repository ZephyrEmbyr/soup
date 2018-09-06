class Amount:

    def __init__(self, quantity, unit):
        self.quantity = quantity
        self.unit = unit

    def replace_quantity(self, new_quantity):
        self.quantity = new_quantity

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (str(self.quantity) + " " + str(self.unit))
