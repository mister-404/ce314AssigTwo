import string
from nltk.corpus import stopwords, movie_reviews


class WordFinder:
    @classmethod
    def bagOfWords(cls, words):
        return dict([word, True] for word in WordFinder.removeUneeded(words))

    @classmethod
    def getReviews(cls, reviewOpinion):
        return [movie_reviews.words(fileid) for fileid in movie_reviews.fileids(reviewOpinion)]

    @classmethod
    def removeUneeded(cls, words):
        # todo: look for if a word is entirely comprised of punctuation (not a useful word to have)
        ENGLISH_STOPWORDS = stopwords.words('english')
        return [word for word in words if (word not in string.punctuation) and (word not in ENGLISH_STOPWORDS)]


class FeatureSet:
    def __init__(self, reviews):
        self.words = [WordFinder.bagOfWords(words) for words in reviews]


negReviews = WordFinder.getReviews('neg')
posReviews = WordFinder.getReviews('pos')

negReviewSet = FeatureSet(negReviews).words
posReviewSet = FeatureSet(posReviews).words

DIVISION_PROPORTION = (len(negReviewSet)+len(posReviewSet)) // 10

testSet = posReviewSet[:DIVISION_PROPORTION] + \
    negReviewSet[:DIVISION_PROPORTION]
trainSet = posReviewSet[DIVISION_PROPORTION:] + \
    negReviewSet[DIVISION_PROPORTION:]

# negativeReviewSet = FeatureSet()
