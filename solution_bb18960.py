from random import shuffle
from nltk import NaiveBayesClassifier
from nltk import classify
import string
from nltk.corpus import stopwords, movie_reviews
import re


class WordTools:
    @classmethod
    def bagOfWords(cls, words):
        return dict([word, True] for word in WordTools.removeUneeded(words))

    @classmethod
    def getReviews(cls, reviewOpinion):
        return [movie_reviews.words(fileid) for fileid in movie_reviews.fileids(reviewOpinion)]

    @classmethod
    def removeUneeded(cls, words):
        cleanedWords = []
        ENGLISH_STOPWORDS = stopwords.words('english')
        for word in words:
            isAStopWord = word in ENGLISH_STOPWORDS
            justPunctuation = re.sub(r"^(\W+|\d+)$", "", word) == ""

            if not justPunctuation and not isAStopWord:
                cleanedWords.append(word)
        return cleanedWords


class FeatureSet:
    def __init__(self, reviews, reviewOpinion):
        self.words = [(WordTools.bagOfWords(words), reviewOpinion)
                      for words in reviews]


negReviews = WordTools.getReviews('neg')
posReviews = WordTools.getReviews('pos')

negReviewSet = FeatureSet(negReviews, 'neg').words
posReviewSet = FeatureSet(posReviews, 'pos').words

DIVISION_PROPORTION = (len(negReviewSet) + len(posReviewSet)) // 10

shuffle(posReviewSet)
shuffle(negReviewSet)

testSet = posReviewSet[:DIVISION_PROPORTION] + \
    negReviewSet[:DIVISION_PROPORTION]
trainSet = posReviewSet[DIVISION_PROPORTION:] + \
    negReviewSet[DIVISION_PROPORTION:]

classifier = NaiveBayesClassifier.train(trainSet)

accuracy = classify.accuracy(classifier, testSet)
print(accuracy)  # Output: 0.7325

print(classifier.show_most_informative_features(10))
