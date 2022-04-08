def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])


def remove_whitechars(text):
    return ' '.join([c.strip() for c in text.split()])
