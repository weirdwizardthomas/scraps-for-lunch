
def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])

class Meal:
    def __init__(self, elements):
        self.sold_out = elements.find('sold-out') is not None
        self.title = ...
        self.price = elements.find('div', 'price').text[:-2] or None
        self.allergens = None

    def __str__(self):
        string = f'{self.title}, {self.price}, {self.allergens}'

        return strike(string) if self.sold_out else string

    def __repr__(self):
        return self.__str__()

