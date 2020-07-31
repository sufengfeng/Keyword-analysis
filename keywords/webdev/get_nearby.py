#!/usr/bin/env python
from nltk.corpus import wordnet
from synonyms import synonyms


def GetKeyWordList(keyWord):
    setKeyWord = set()
    ch_near = synonyms.nearby(keyWord)
    word_list = list(ch_near)[0]
    value_list = list(ch_near)[1]
    for i in range(len(word_list)):
        if value_list[i] > 0.5:
            setKeyWord.add(word_list[i])

    for i in range(5):
        try:
            strFind = keyWord + ".n.0" + str(i)
            lemmaList = wordnet.synset(strFind).lemma_names()
            for nearWord in lemmaList:
                setKeyWord.add(nearWord)
        except Exception as e:
            print(e)
    en_near = wordnet.synsets(keyWord)

    # print(setKeyWord)
    return setKeyWord


if __name__ == "__main__":
    # ch = synonyms.nearby("你好")
    # print(ch)
    #
    # en = wordnet.synsets('car')
    # for lem in en:
    #     print(lem.lemma_names())
    # a = wordnet.synset('car.n.01').lemma_names()
    #
    # b = wordnet.synset('car.n.01').definition()         #解释
    #
    # c = wordnet.synset('car.n.01').examples()           #举例造句
    #
    #
    # ch = synonyms.nearby("hello")
    # print(ch)
    #
    # test = wordnet.synsets('你好')
    # for lem in test:
    #     print(lem.lemma_names())
    # print(en)

    # GetKeyWordList("test")
    GetKeyWordList("check")
    print("test")
    # getNearBy()
