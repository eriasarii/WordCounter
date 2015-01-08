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