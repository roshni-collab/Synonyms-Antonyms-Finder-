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

print(f"Synonyms of '{word}':", ", ".join(synonyms) if synonyms else "None found")
print(f"Antonyms of '{word}':", ", ".join(antonyms) if antonyms else "None found")

word = word.lower()
