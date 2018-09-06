class Amount:
    def __init__(self, quantity, unit):
        self.quantity = quantity
        self.unit = unit

    def replace_quantity(self, new_quantity):
        self.quantity = new_quantity
