import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from src.entity.kathmandu.meal import Meal
from src.entity.version import Version

VERSION = Version('1.0', 2022, 4, 4)
URL = 'https://www.restauracekathmandu.cz/denni-menu'

DAYS = [
    'MONDAY',
    'TUESDAY',
    'WEDNESDAY',
    'THURSDAY',
    'FRIDAY'
]

DAY_PATTERN = '|'.join(map(re.escape, DAYS))


def get_menu():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    items = [x.text.strip() for x in soup.find(itemprop='articleBody').find_all('span')]
    concatenated_items = ';'.join(items).replace('\xa0', '')
    filtered_items = re.split(DAY_PATTERN, concatenated_items, flags=re.IGNORECASE)[2::2]

    today = filtered_items[datetime.today().weekday()].split(';')[6:-1]

    today_no_descriptions = [x for x in today if '(' not in x or ')' not in x]

    return {'Všechna jídla': [Meal(item) for item in today_no_descriptions]}
