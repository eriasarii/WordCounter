#!/usr/bin/env python
from operator import itemgetter

__author__ = 'Eriasarii'


class WordListManager:
    def __init__(self):
        self.__listWord = []

    def separateWord(self, row):
        return row.split(" ")

    def checkWord(self, word):
        for i in self.__listWord:
            if (i[0] == word):
                return False
        return True

    def addWord(self, word):
        self.__listWord.append([word, 1])

    def updateList(self, word):
        for i in self.__listWord:
            if (i[0] == word):
                i[1] += 1

    def getListWord(self):
        return self.__listWord

    def sortList(self):
        self.__listWord.sort(key=itemgetter(1), reverse=True)