# deskriptive Analyse

import os
from nltk.tokenize import word_tokenize

male_corpus_directory = '/Users/a1/Documents/0. UNI/6. SS 2023/Forsch_design/projekt/output_dta_kernkorpus_1800-1899/male_txt'
female_corpus_directory = '/Users/a1/Documents/0. UNI/6. SS 2023/Forsch_design/projekt/output_dta_kernkorpus_1800-1899/female_txt'

def calculate_tokens_and_types(directory):
    tokens = []
    types = set()

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = word_tokenize(text)
            tokens.extend(words)
            types.update(words)

    return tokens, types

male_tokens, male_types = calculate_tokens_and_types(male_corpus_directory)
female_tokens, female_types = calculate_tokens_and_types(female_corpus_directory)

total_male_tokens = len(male_tokens)
total_male_types = len(male_types)

total_female_tokens = len(female_tokens)
total_female_types = len(female_types)

print(f'Gesamtanzahl der Tokens in männlichem Korpus: {total_male_tokens}')
print(f'Gesamtanzahl der Types in männlichem Korpus: {total_male_types}')

print(f'Gesamtanzahl der Tokens in weiblichem Korpus: {total_female_tokens}')
print(f'Gesamtanzahl der Types in weiblichem Korpus: {total_female_types}')

