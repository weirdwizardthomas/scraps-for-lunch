class AbstractMeal:
    def __init__(self):
        self.title = None
        self.price = None
        self.allergens = []

    def __str__(self):
        return f'{self.title}, {self.price}, {self.allergens}'
