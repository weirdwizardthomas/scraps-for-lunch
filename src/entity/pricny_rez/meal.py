from src.entity.abstract_meal import AbstractMeal


class Meal(AbstractMeal):
    def __init__(self, elements):
        super().__init__()
        price_element = elements.find('p', class_='cena')

        # Some items, such as soups, do not have their own individual price tags
        self.price = price_element.text.split(',-')[0].strip() if price_element else None

        split_title = elements.find('p', class_='nazev').text.split('/')
        self.title = split_title[0].strip()

        if len(split_title) > 1:
            self.allergens = split_title[1].strip().split(',')
