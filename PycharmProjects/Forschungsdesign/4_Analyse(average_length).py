# mit NLTK

import os
import re
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')


def durchschnittliche_satzlaenge(text):
    sentences = sent_tokenize(text)
    num_sentences = len(sentences)

    total_sentence_length = sum(len(sentence.split()) for sentence in sentences)
    average_length = total_sentence_length / num_sentences
    return average_length


corpus_directory_m = "/Users/a1/Documents/0. UNI/6. SS 2023/Forsch_design/projekt/output_dta_kernkorpus_1800-1899/male_txt"
corpus_directory_w = "/Users/a1/Documents/0. UNI/6. SS 2023/Forsch_design/projekt/output_dta_kernkorpus_1800-1899/female_txt"

# Durchschnittliche Satzlänge für Männer
gesamttext_m = ''
for filename in os.listdir(corpus_directory_m):
    if filename.endswith('.txt'):
        file_path = os.path.join(corpus_directory_m, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            gesamttext_m += text

average_length_m = durchschnittliche_satzlaenge(gesamttext_m)

# Durchschnittliche Satzlänge für Frauen
gesamttext_w = ''
for filename in os.listdir(corpus_directory_w):
    if filename.endswith('.txt'):
        file_path = os.path.join(corpus_directory_w, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            gesamttext_w += text

average_length_w = durchschnittliche_satzlaenge(gesamttext_w)
print(f"Durchschnittliche Satzlänge für den gesamten Text von Männern: {average_length_m:.2f} Wörter")
print(f"Durchschnittliche Satzlänge für den gesamten Text von Frauen: {average_length_w:.2f} Wörter")