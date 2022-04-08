import bs4
import requests
from bs4 import BeautifulSoup, NavigableString, Tag

from src.entity.version import Version
from src.util import remove_whitechars

VERSION = Version('1.0', 2022, 3, 31)

URL = 'https://www.lemon.cz/en/lunch-menu-2/'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

current_element = soup.find('h2', class_='day-now')

for x in (current_element.find_next_siblings('div', class_='lunch-food-item'))[:3]:
    print(remove_whitechars(x.find('p').text))
