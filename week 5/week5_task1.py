import string

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "text.txt")


word_freq = {}
lines_count = 0
words_count = 0

with open(FILE_PATH, "r", encoding="utf-8") as file:



    for line in file:
        lines_count += 1
        clean_line = line.translate(str.maketrans("", "", string.punctuation)).lower()
        words = clean_line.split()
        words_count += len(words)
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

with open("analysis.txt", "w", encoding="utf-8") as out:
    out.write(f"Total lines: {lines_count}\n")
    out.write(f"Total words: {words_count}\n")
    out.write("Word frequency:\n")
    for word in sorted(word_freq):
        out.write(f"{word}: {word_freq[word]}\n")
