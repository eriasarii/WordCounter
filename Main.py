#!/usr/bin/env python
from FileManager import FileManager
from WordListManager import WordListManager

__author__ = 'Eriasarii'

fileManager = FileManager("test")
quantityRows = fileManager.countRows()
wordManager = WordListManager()

for i in range(1, quantityRows + 1):
    rowFile = fileManager.loadRow(i).strip()
    separatedWords = wordManager.separateWord(rowFile)
    for j in separatedWords:
        if (wordManager.checkWord(j)):
            wordManager.addWord(j)
        else:
            wordManager.updateList(j)

print wordManager.getListWord()
wordManager.sortList()
print wordManager.getListWord()


