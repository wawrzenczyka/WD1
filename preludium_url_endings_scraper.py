import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_page_soup(group_name, page_number):
    page_content = requests.get(
        "https://projekty.ncn.gov.pl/index.php?jednostka=&jednostka_miasto=&jednostka_wojewodztwo=&kierownik=&kierownik_plec=&kierownik_tytul=&status=&projekt=&kwotaprzyznanaod=&kwotaprzyznanado=&typkonkursu=2&konkurs=&grupa="
        + group_name + "&panel=&slowokluczowe=&aparatura=&strona=" + str(page_number))
    return BeautifulSoup(page_content.text, features="html.parser")


def append_pages_strings():
    rows = soup.select('div[id=wynikiwyszukiwarki]')[0] \
        .findAll('ol')[0] \
        .findAll('li')
    for row in rows:
        link = row.select('a')[0]['href']
        preludium_pages.append(link)


def get_group_page_count():
    pagination = soup.select('div[class=pagination]')[0] \
        .findAll('a')
    count = pagination[len(pagination) - 1]
    return int(count.text)


preludium_pages = []
groups = ['HS', 'NZ', 'ST']

for group in groups:
    soup = get_page_soup(group, 1)
    append_pages_strings()
    pages_count = get_group_page_count()

    for page in range(2, pages_count + 1):
        soup = get_page_soup(group, page)
        append_pages_strings()


df = pd.DataFrame({'Pages url endings': preludium_pages})
df.to_csv('preludium_url_endings.csv', index=False, encoding='utf-8')
