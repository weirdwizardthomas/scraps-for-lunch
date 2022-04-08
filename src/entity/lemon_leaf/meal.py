from src.entity.abstract_meal import AbstractMeal
from src.util import remove_whitechars


class Meal(AbstractMeal):
    def __init__(self, elements):
        super().__init__()

        self.title = remove_whitechars(elements.find('p').text)

        is_not_soup = elements.find('span', text='Soup') is None
        self.price = 159 if is_not_soup else '49 or 35 in menu'
