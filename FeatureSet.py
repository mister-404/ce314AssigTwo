from WordTools import WordTools


class FeatureSet:
    def __init__(self, reviews, reviewOpinion):
        self.words = [(WordTools.bagOfWords(words), reviewOpinion)
                      for words in reviews]
