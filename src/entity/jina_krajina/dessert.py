from src.entity.jina_krajina.meal import Meal


class Dessert(Meal):
    def __init__(self, elements):
        super().__init__(elements)

        # Strong assumption that allergens are always enclosed in brackets
        split_title = elements.find('div', 'title').text.split('(')

        if len(split_title) > 1:
            self.allergens = (split_title[1]
                              .strip()
                              .strip('()')  # closing bracket
                              .split(',')  # allergen values are delimited by commas
                              )

        self.title = split_title[0].strip()
