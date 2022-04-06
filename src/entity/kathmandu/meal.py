from src.entity.abstract_meal import AbstractMeal


class Meal(AbstractMeal):
    def __init__(self, elements):
        super().__init__()
        split_text = elements.strip().split()

        self.title = ' '.join(split_text[:-2])
        self.price = split_text[-2].replace(',-', '')
        self.allergens = []
