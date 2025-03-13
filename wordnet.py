from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')

word = input("Enter a word: ")

synsets = wordnet.synsets(word)

synonyms = set()
for syn in synsets:
    for lemma in syn.lemmas():
        synonyms.add(lemma.name())

antonyms = set()
for syn in synsets:
    for lemma in syn.lemmas():
        if lemma.antonyms():
            antonyms.add(lemma.antonyms()[0].name())
