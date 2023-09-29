import os
import requests
import xml.etree.ElementTree as et
from bs4 import BeautifulSoup
from lxml import etree

# Funktion zum Herausfinden des Geschlechtes
def get_gender_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')

        table = soup.find('table', {'id': 'fullRecordTable'})
        gender_element1 = table.select('tr:nth-of-type(4) td:nth-of-type(2)')
        gender_element2 = table.select('tr:nth-of-type(5) td:nth-of-type(2)')

        if "männlich" in str(gender_element1) or "männlich" in str(gender_element2):
            return "männlich"
        elif "weiblich" in str(gender_element1) or "weiblich" in str(gender_element2):
            return "weiblich"
    return None

corpus_directory = r"/Users/a1/Downloads/dta_komplett_1800-1899_2021-05-13"
output_directory = r"/Users/a1/Downloads/output"


male_folder = os.path.join(output_directory, "männlich")
female_folder = os.path.join(output_directory, "weiblich")
os.makedirs(male_folder, exist_ok=True)
os.makedirs(female_folder, exist_ok=True)

for filename in os.listdir(corpus_directory):
    if filename.endswith(".xml"):
        file_path = os.path.join(corpus_directory, filename)

        with open(file_path, 'rb') as file:
            xml_content = file.read()

        tree = etree.fromstring(xml_content)

        namespaces = {'m': 'http://www.tei-c.org/ns/1.0'}
        persName_elements = tree.xpath('//m:author/m:persName', namespaces=namespaces)
        ref_values = set([persName.get('ref') for persName in persName_elements])

        if ref_values:
            author_url = next(iter(ref_values))
            if author_url:
                gender = get_gender_from_url(author_url)

                if gender:
                    if gender == "männlich":
                        destination_folder = male_folder
                    elif gender == "weiblich":
                        destination_folder = female_folder

                    destination_path = os.path.join(destination_folder, filename)
                    os.rename(file_path, destination_path)
                    print(f"Datei: {filename}, Geschlecht: {gender}, Zielordner: {destination_folder}")
                else:
                    print(f"Datei: {filename}, keine gültige URL für Geschlecht.")
        else:
            print(f"Datei: {filename}, kein 'ref'-Attribut in 'persName' gefunden.")

print("Dateien wurden in die entsprechenden Ordner verschoben.")
