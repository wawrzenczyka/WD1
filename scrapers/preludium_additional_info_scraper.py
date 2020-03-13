import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def scrap_title(soup):
    return soup.select('h2')[0].text


def scrap_id(soup):
    return soup.select('p')[0].text


def scrap_descriptors(soup):
    descriptors = []
    for descriptor in soup.select('li'):
        descriptors.append(descriptor.text.split(':')[0])
    return descriptors


def scrap_manager(soup):
    manager_with_title = soup.select('a[title="Kliknij w link aby zobaczyć inne projekty tego kierownika"]')[0].text
    first_upper_case_letter = re.search("[A-Z]", manager_with_title).start()
    manager_title, manager_name = manager_with_title[:first_upper_case_letter - 1], manager_with_title[
                                                                                    first_upper_case_letter:]
    return manager_title, manager_name


def scrap_publications(soup):
    publications_types = soup.select('ul[class=rodzajepublikacji]')
    magazines_publications = 0
    post_conference_publications = 0
    books_publications = 0
    if len(publications_types) != 0:
        for publications_type in publications_types[0].select('li'):
            count = publications_type.text.split("(")[1].split(")")[0]
            if publications_type.text.startswith("Publikacje w czasopismach"):
                magazines_publications = count
            elif publications_type.text.startswith("Teksty w publikacjach pokonferencyjnych"):
                post_conference_publications = count
            elif publications_type.text.startswith("Publikacje książkowe"):
                books_publications = count
            else:
                print("Nieznany rodzaj publikacji " + publications_type.text)
    return magazines_publications, post_conference_publications, books_publications


def scrap_key_words(soup):
    key_words = []
    words = soup.select('span[class=frazy]')[0].select('a')
    for word in words:
        key_words.append(word.text)
    return key_words


def scrap_units(soup):
    pages = soup.select('div[class=strona]')
    unit = ""
    voivodeship = ""
    for page in pages:
        unit_page = page.select('p[style="line-height: 24px;padding-top: 4px;"]')
        if len(unit_page) == 0:
            continue
        unit = unit_page[0].text
        voivodeship = page.select('p[style="padding-top:4px;"]')[0].text.replace("woj. ", "")
        break
    return unit, voivodeship


def scrap_equipment(soup):
    equipment_string = ""
    equipment_count = 0
    equipment_cost = 0

    equipment = soup.find(lambda elm: elm.name == "h2" and "Zakupiona aparatura" in elm.text)

    if equipment is not None:
        equipment = equipment.findNext('ol').select('li')
        equipment_count = len(equipment)
        for item in equipment:
            item_name, item_price = item.text.split(". Za kwotę ")

            if len(equipment_string) == 0:
                equipment_string = item_name
            else:
                equipment_string += ", " + item_name

            if (item_price.find(" PLN")) == -1:
                important = soup.select('div[class=important]')[0]
                title = scrap_title(important)
                print(title + " price: " + item_price)
            else:
                price_in_pln = int(item_price.replace("PLN", "").replace(" ", ""))
                equipment_cost += price_in_pln

    return equipment_string, equipment_count, equipment_cost


def get_page_soup(url_ending):
    url = "https://projekty.ncn.gov.pl/index.php" + url_ending
    page_content = requests.get(url)
    return BeautifulSoup(page_content.text, features="html.parser")


def add_additional_data(url_ending):
    soup = get_page_soup(url_ending)
    important = soup.select('div[class=important]')[0]

    title = scrap_title(important)
    id_long = scrap_id(important)
    descriptors = scrap_descriptors(important)
    manager_title, manager_name = scrap_manager(soup)
    magazines_publications, post_conference_publications, books_publications = scrap_publications(soup)
    key_words = scrap_key_words(soup)
    unit, voivodeship = scrap_units(soup)
    equipment_string, equipment_count, equipment_cost = scrap_equipment(soup)

    additional_info_row = {
        'Id': id_long,
        'Title': title,
        'Magazines publications': magazines_publications,
        'Book publications': books_publications,
        'Post-conference publications': post_conference_publications,
        'Equipment': equipment_string,
        'Equipment cost': equipment_cost,
        'Equipment count': equipment_count,
        'Manager': manager_name,
        'Managers title': manager_title,
        'Unit': unit,
        'Voivodeship': voivodeship
    }

    key_words_rows = []
    for key_word in key_words:
        key_words_rows.append({
            'Id': id_long,
            'Key word': key_word
        })

    descriptor_rows = []
    for descriptor in descriptors:
        descriptor_rows.append({
            'Id': id_long,
            'Descriptors': descriptor
        })
    return additional_info_row, key_words_rows, descriptor_rows


column_names_additional_info = [
    'Id',
    'Title',
    'Magazines publications',
    'Book publications',
    'Post-conference publications',
    'Equipment',
    'Equipment cost',
    'Equipment count',
    'Manager',
    'Managers title',
    'Unit',
    'Voivodeship'
]

column_names_key_words = [
    'Id',
    'Key word'
]

column_names_descriptors = [
    'Id',
    'Descriptors'
]

df_additional_info = pd.DataFrame(columns=column_names_additional_info)
df_key_words = pd.DataFrame(columns=column_names_key_words)
df_descriptors = pd.DataFrame(columns=column_names_descriptors)

df = pd.read_csv("scrapers/data/preludium_url_endings.csv")

for i in range(0, 4):
    additional_info_row, key_words_row, descriptor_row = add_additional_data(df['Pages url endings'][i])
    df_additional_info = df_additional_info.append(additional_info_row, ignore_index=True)
    df_key_words = df_key_words.append(key_words_row, ignore_index=True)
    df_descriptors = df_descriptors.append(descriptor_row, ignore_index=True)

df_additional_info.to_csv("data/preludium_additional_info.csv", index=False)
df_key_words.to_csv("data/preludium_key_words.csv", index=False)
df_descriptors.to_csv("data/preludium_descriptors.csv", index=False)
