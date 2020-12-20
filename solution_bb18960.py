from random import shuffle
from nltk import NaiveBayesClassifier, classify
from FeatureSet import FeatureSet
from WordTools import WordTools

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

print("Accuracy of this model", classify.accuracy(classifier, testSet))

print(classifier.show_most_informative_features(10))
