'''
Loads in the most common names from the https://www.ssa.gov/oact/babynames/limits.html
'''
namesDataPath = "./res/commonNames.txt"


class CommonNamesFinder:
    def __init__(self):
        self.names = []
        namesFile = open(namesDataPath, 'r')
        lines = namesFile.readlines()

        for line in lines:
            splitLine = line.split(",")
            self.names.append(splitLine[0])
