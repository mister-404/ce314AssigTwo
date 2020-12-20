import csv

namesDataPath = "./res/commonNames.txt"


class CommonNamesFinder:
    def __init__(self):
        '''
        Loads in the most common names from the
        https://www.ssa.gov/oact/babynames/limits.html
        '''
        self.names = []

        with open(namesDataPath, 'r') as namesFile:
            reader = csv.reader(namesFile)
            for row in reader:
                self.names.append(row[0].lower())
