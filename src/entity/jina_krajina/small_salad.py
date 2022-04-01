from src.entity.jina_krajina.meal import Meal


class SmallSalad(Meal):
    def __init__(self, elements):
        super().__init__(elements)

        self.title = (elements.find('div', 'title').text
            .strip()
            .split(' ')[0])

        self.allergens = None
