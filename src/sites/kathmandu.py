import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from src import constant
from src.entity.kathmandu.meal import Meal
from src.entity.version import Version

VERSION = Version('1.1', 2022, 4, 4)
URL = 'https://www.restauracekathmandu.cz/denni-menu'

DAY_PATTERN = '|'.join(map(re.escape, constant.DAYS))


def get_menu():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    items = [x.text.strip() for x in soup.find(itemprop='articleBody').find_all('span') if x.text]

    filtered = [x for x in items if x]
    concatenated_items = ';'.join(filtered)
    concatenated_items = concatenated_items.replace('\xa0', '')

    split_by_day = re.split(DAY_PATTERN, concatenated_items, flags=re.IGNORECASE)[2::2]

    today = split_by_day[datetime.today().weekday()].split(';')[6:-1]

    today_no_descriptions = [x for x in today if '(' not in x or ')' not in x]

    return {'Všechna jídla': [Meal(item) for item in today_no_descriptions]}
