import collections
from random import shuffle
from nltk import NaiveBayesClassifier, classify
from nltk.metrics.scores import (precision, recall)
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

print("Accuracy:", classify.accuracy(classifier, testSet))

refsets = collections.defaultdict(set)
testsets = collections.defaultdict(set)

for i, (feats, label) in enumerate(testSet):
    refsets[label].add(i)
    observed = classifier.classify(feats)
    testsets[observed].add(i)

precisionVal = precision(refsets['pos'], testsets['pos'])
recallVal = recall(refsets['pos'], testsets['pos'])
fMeasureVal = (2 * precisionVal * recallVal) / (precisionVal + recallVal)

print("Precision:", precisionVal)
print("Recall:", recallVal)
print("F-Score:", fMeasureVal)

print(classifier.show_most_informative_features(10))
