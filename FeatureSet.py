'''
Provides functionality for a FeatureSet object that can
then be used for a classifier

bb18960
'''

from WordTools import WordTools


class FeatureSet:
    def __init__(self, reviews, reviewOpinion):
        self.words = [(WordTools.bothBags(words), reviewOpinion)
                      for words in reviews]
