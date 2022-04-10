from src.entity.abstract_meal import AbstractMeal
from src.string_util import strike


class Meal(AbstractMeal):
    def __init__(self, elements):
        super().__init__()

        self.sold_out = elements.find('sold-out') is not None
        self.title = ...
        self.price = elements.find('div', 'price').text[:-2] or None
        self.allergens = []

    def __str__(self):
        string = f'{self.title}, {self.price}, {self.allergens}'

        return strike(string) if self.sold_out else string
