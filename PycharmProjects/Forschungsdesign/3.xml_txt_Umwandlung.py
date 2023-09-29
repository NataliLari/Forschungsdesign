# male
import os
import re
from xml.etree import ElementTree as ET

input_directory = "/Users/a1/Documents/0. UNI/6. SS 2023/Forsch_design/projekt/output_dta_kernkorpus_1800-1899/male_selected_last"
output_directory = "/Users/a1/Documents/0. UNI/6. SS 2023/Forsch_design/projekt/output_dta_kernkorpus_1800-1899/male_txt"

# Funktion zum Extrahieren von Text
def extract_text(element):
    return ' '.join(element.itertext())

# Funktion zum Entfernen der unerwünschten Tags und Inhalte
def remove_unwanted_tags(text):
    text = re.sub(r'<fw.*?>.*?</fw>', '', text)  # Entfernt Seitennummer
    return text

for filename in os.listdir(input_directory):
    if filename.endswith(".xml"):
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.txt")

        tree = ET.parse(input_path)
        root = tree.getroot()

        body_element = root.find(".//{http://www.tei-c.org/ns/1.0}body")
        if body_element is not None:
            extracted_text = extract_text(body_element)
        else:
            extracted_text = ""

        cleaned_text = remove_unwanted_tags(extracted_text)
        cleaned_text = re.sub(r'—\s*\d+\s*—', '', cleaned_text)

        with open(output_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(cleaned_text)

        print(f"Datei {filename} wurde verarbeitet und als {output_path} gespeichert.")


