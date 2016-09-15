
import random

with open("/usr/share/dict/words") as word_list:
    random_word = word_list.read().lower().split()
