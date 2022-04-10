from src.entity.abstract_meal import AbstractMeal


class Meal(AbstractMeal):
    def __init__(self, elements):
        super().__init__()

        split_title = elements.find('h3').text.split(' – ')

        # If split by delimiter, take the [1] elements, otherwise take the [0] element
        self.title = split_title[len(split_title) > 1].strip()
        self.price = elements.find('span', class_='price').text.split(' ')[0]
