class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        temp = str(self.amount) + " " + self.name
        return temp
