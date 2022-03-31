from bs4 import BeautifulSoup
import requests

from src.entity.jina_krajina import *

URL = 'https://reznicka.jinakrajina.cz/cs/poledni-menu/'

ITEM_WRAPPER_CLASS_TAG = 'food-item-wrapper'
CATEGORY_CLASS_TAG = 'food-block'


def get_menu():
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    soups, salads, main_menu, salad_menu, desserts = soup.find_all('div', class_=CATEGORY_CLASS_TAG)

    soup_items = soups.find_all('div', ITEM_WRAPPER_CLASS_TAG)
    main_menu_items = main_menu.find_all('div', ITEM_WRAPPER_CLASS_TAG)
    salad_items = salad_menu.find_all('div', ITEM_WRAPPER_CLASS_TAG)
    small_salad_items = salads.find_all('div', ITEM_WRAPPER_CLASS_TAG)
    dessert_items = desserts.find_all('div', ITEM_WRAPPER_CLASS_TAG)

    return {
        'Polévky': [Soup(item) for item in soup_items],
        'Malý salát místo polévky': [SmallSalad(item) for item in small_salad_items],
        'Hlavní chod': [MainMeal(item) for item in main_menu_items],
        'Saláty': [MainMeal(item) for item in salad_items],
        'Dezerty': [Dessert(item) for item in dessert_items]
    }
