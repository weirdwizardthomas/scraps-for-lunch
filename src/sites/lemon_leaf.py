import requests
from bs4 import BeautifulSoup

from src.entity.lemon_leaf.meal import Meal
from src.entity.version import Version

VERSION = Version('1.0', 2022, 4, 10)

URL = 'https://www.lemon.cz/en/lunch-menu-2/'


def get_menu():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    current_element = soup.find('h2', class_='day-now')

    menu_items = current_element.find_next_siblings('div', class_='lunch-food-item')[:3]

    return {
        'Všechna jídla': [Meal(item) for item in menu_items]
    }
