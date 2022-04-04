class Meal:
    def __init__(self, elements):
        elements = elements.strip()
        squished_spaces = ' '.join((elements.split()))
        split_text = squished_spaces.split()

        self.title = ' '.join(split_text[:-2])
        self.price = split_text[-2].replace(',-', '')
        self.allergens = []

    def __str__(self):
        return f'{self.title}, {self.price}, {self.allergens}'
