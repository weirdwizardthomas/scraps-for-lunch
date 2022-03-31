

class Meal:
    def __init__(self, elements):
        self.sold_out = elements.find('sold-out') is None
        self.title = ...
        self.price = elements.find('div', 'price').text[:-2] or None
        self.allergens = None

    def __str__(self):
        return f'{self.title}, {self.sold_out}, {self.price}, {self.allergens}'

    def __repr__(self):
        return self.__str__()

