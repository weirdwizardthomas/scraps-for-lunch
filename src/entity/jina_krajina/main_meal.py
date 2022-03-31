from src.entity.jina_krajina.meal import Meal


class MainMeal(Meal):
    def __init__(self, elements):
        super().__init__(elements)

        # Main dish title starts with a number followed by a full stop, e.g. '2.'
        self.title = (elements.find('div', 'title').text[2:]
                      .strip())

        # Allergens in main courses are included in the description, within ( ) brackets
        self.allergens = (elements.find('div', 'description').text
                          .split('(')[-1]  # Opening bracket
                          .strip()  # white chars
                          .strip('()')  # Enclosing bracket
                          .split(',')  # List of allergens is delimited by ','
                          )
