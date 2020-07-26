#!/usr/bin/env python
from nltk.corpus import wordnet as wn
from synonyms import synonyms

if __name__ == "__main__":
    ch = synonyms.nearby("你好")
    print(ch)

    en = wn.synsets('fly')
    for lem in en:
        print(lem.lemma_names())
    a = wn.synset('car.n.01').lemma_names()

    b = wn.synset('car.n.01').definition()

    c = wn.synset('car.n.01').examples()

    print(en)
    print("test")
    # getNearBy()