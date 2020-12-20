'''
Looks at a given results file and then
finds averages on the data items

bb18960
'''

import csv


class ResultsAnalyser:
    def __init__(self, fileLoc):
        self.records = []
        with open(fileLoc, 'r') as resultsFile:
            resultsFileReader = csv.reader(resultsFile)
            firstRow = True
            for row in resultsFileReader:
                if firstRow:
                    firstRow = False
                else:
                    self.records.append(row)

    def getAvgs(self):
        rowCount = len(self.records)
        accSum = 0
        precSum = 0
        recSum = 0
        fScoreSum = 0

        for row in self.records:
            accSum += float(row[0])
            precSum += float(row[1])
            recSum += float(row[2])
            fScoreSum += float(row[3])

        ROUNDING_ACCURACY = 3

        return (
            round(accSum/rowCount, ROUNDING_ACCURACY),
            round(precSum/rowCount, ROUNDING_ACCURACY),
            round(recSum/rowCount, ROUNDING_ACCURACY),
            round(fScoreSum/rowCount, ROUNDING_ACCURACY)
        )
