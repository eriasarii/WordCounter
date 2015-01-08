#!/usr/bin/env python
import linecache

__author__ = 'Eriasarii'


class FileManager:
    def __init__(self, fileName):
        self.fileName = fileName

    def loadRow(self, rowNumber):
        return linecache.getline(self.fileName, rowNumber)

    def countRows(self):
        count = -1
        for count, wiersz in enumerate(open(self.fileName, 'rU')):  # universal newlines
            pass
        count += 1

        return count

    def saveResult(self, name, listToSave):
        file = open(name, "w")
        for i in listToSave:
            file.write(i[0] + " == ")
            file.write(i[1].__str__() + "\n")
        file.close()