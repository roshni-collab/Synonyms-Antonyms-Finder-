from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')

word = input("Enter a word: ")

synsets = wordnet.synsets(word)
