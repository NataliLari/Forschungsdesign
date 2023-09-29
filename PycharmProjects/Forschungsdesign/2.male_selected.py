import os
from lxml import etree

input_directory = "/Users/a1/Documents/0. UNI/6. SS 2023/Forsch_design/projekt/output_dta_kernkorpus_1800-1899/männlich"

output_directory = "/Users/a1/Documents/0. UNI/6. SS 2023/Forsch_design/projekt/output_dta_kernkorpus_1800-1899/male_selected"
os.makedirs(output_directory, exist_ok=True)
namespaces = {'tei': 'http://www.tei-c.org/ns/1.0'}

# Erlaubte Veröffentlichungsorte
allowed_places = ["Berlin", "Leipzig", "Jena", "Frankfurt (Main)", "Heidelberg"]

# Analyse von Dateien im Ordner "männlich"
for filename in os.listdir(input_directory):
    if filename.endswith(".xml"):
        file_path = os.path.join(input_directory, filename)

        with open(file_path, 'rb') as file:
            xml_content = file.read()

        tree = etree.fromstring(xml_content)
        pub_place_elements = tree.xpath('//tei:fileDesc/tei:sourceDesc/tei:biblFull/tei:publicationStmt/tei:pubPlace',
                                        namespaces=namespaces)

        if pub_place_elements:
            pub_place = pub_place_elements[0].text

        pub_year = int(filename.split("_")[-1].split(".")[0])

        if 1800 <= pub_year <= 1899 and pub_place in allowed_places:
            selected_path = os.path.join(output_directory, filename)
            os.rename(file_path, selected_path)
            print(f"Datei: {filename}, erfüllt die Kriterien, verschoben nach: {output_directory}")
        else:
            print(f"Datei: {filename}, erfüllt die Kriterien für das Jahr nicht.")

print("Dateien, die den Kriterien entsprechen, wurden in den ausgewählten Ordner verschoben.")