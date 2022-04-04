from src.entity.abstract_meal import AbstractMeal


class Meal(AbstractMeal):
    def __init__(self, elements):
        super().__init__()
        elements = elements.strip()
        squished_spaces = ' '.join((elements.split()))
        split_text = squished_spaces.split()

        self.title = ' '.join(split_text[:-2])
        self.price = split_text[-2].replace(',-', '')
        self.allergens = []
