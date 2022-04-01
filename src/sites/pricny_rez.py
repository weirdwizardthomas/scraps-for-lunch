from bs4 import BeautifulSoup
import requests


from src.entity.pricny_rez.meal import Meal
from src.entity.version import Version

VERSION = Version('1.0', 2022, 3, 31)
URL = 'https://www.pricnyrez.cz/cs/poledni-menu/'


def get_menu():
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    menu_items = soup.find(id='content').find_all('div', class_='menuItem')

    return {
        'Všechna jídla': [Meal(item) for item in menu_items]
    }
