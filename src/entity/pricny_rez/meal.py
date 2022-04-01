class Meal:
    def __init__(self, elements):
        price_element = elements.find('p', class_='cena')

        # Some items, such as soups, do not have their own individual price tags
        self.price = price_element.text.split(',-')[0].strip() if price_element else None

        split_title = elements.find('p', class_='nazev').text.split('/')
        self.title = split_title[0].strip()

        # Some items do not have allergens in their title
        self.allergens = split_title[1].strip().split(',') if len(split_title) > 1 else None

    def __str__(self):
        return f'{self.title}, {self.price}, {self.allergens}'
