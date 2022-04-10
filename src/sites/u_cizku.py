import requests
from bs4 import BeautifulSoup
import datetime

from src.entity.u_cizku.meal import Meal
from src.entity.version import Version

VERSION = Version('1.0', 2022, 4, 10)
URL = 'https://www.ucizku.cz/dennimenu.php'

TODAY = datetime.datetime.today().date()


def is_today(date):
    text_split = date.text.split(' ')[1]
    date = datetime.datetime.strptime(text_split, '%d.%m.%Y')
    return date.date() == TODAY


def get_menu():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    days_headers = [day for day in soup.find_all('span', class_='kategorienazev') if is_today(day)]
    today_header = days_headers[0]

    menu_items = today_header.next_sibling.find_all('div', class_='jidlo_item')

    if not menu_items:
        raise ValueError('No menu found for today')

    return {
        'Všechna jídla': [Meal(item) for item in menu_items]
    }
