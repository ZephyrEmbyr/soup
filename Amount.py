class Amount:
<<<<<<< HEAD
    def __init__(self, quantity):
        self.quantity = quantity
=======
    def __init__(self, quantity, unit):
        self.quantity = quantity
        self.unit = unit

    def replace_quantity(self, new_quantity):
        self.quantity = new_quantity

>>>>>>> dabcced74f0b0c41ca7c909ccd99b5f4a6b388dd
