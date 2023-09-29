# TTR-Methode

import os
import nltk
from nltk.tokenize import word_tokenize

def calculate_ttr(text):
    tokens = word_tokenize(text)
    types = set(tokens)
    ttr = len(types) / len(tokens)
    return ttr

male_folder = "/Users/a1/Documents/0. UNI/6. SS 2023/Forsch_design/projekt/output_dta_kernkorpus_1800-1899/male_txt"
female_folder = "/Users/a1/Documents/0. UNI/6. SS 2023/Forsch_design/projekt/output_dta_kernkorpus_1800-1899/female_txt"

male_ttr_values = []
female_ttr_values = []

# männliche Texte
for filename in os.listdir(male_folder):
    with open(os.path.join(male_folder, filename), 'r', encoding='utf-8') as file:
        text = file.read()
        ttr = calculate_ttr(text)
        male_ttr_values.append(ttr)

# weibliche Texte
for filename in os.listdir(female_folder):
    with open(os.path.join(female_folder, filename), 'r', encoding='utf-8') as file:
        text = file.read()
        ttr = calculate_ttr(text)
        female_ttr_values.append(ttr)

avg_ttr_male = sum(male_ttr_values) / len(male_ttr_values)
avg_ttr_female = sum(female_ttr_values) / len(female_ttr_values)

print(f"Durchschnittliches Typ-Token-Verhältnis (männlich):, {avg_ttr_male:.4f}")
print(f"Durchschnittliches Typ-Token-Verhältnis (weiblich):, {avg_ttr_female:.4f}")