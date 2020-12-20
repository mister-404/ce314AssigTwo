import collections
from random import shuffle
from nltk import NaiveBayesClassifier, classify
from nltk.metrics.scores import (precision, recall)
from FeatureSet import FeatureSet
from WordTools import WordTools
from ResultsAnalyser import ResultsAnalyser
import csv

RESULT_FILE_LOC = "./results.csv"

negReviews = WordTools.getReviews('neg')
posReviews = WordTools.getReviews('pos')

negReviewSet = FeatureSet(negReviews, 'neg').words
posReviewSet = FeatureSet(posReviews, 'pos').words

DIVISION_PROPORTION = (len(negReviewSet) + len(posReviewSet)) // 20
# takes 20 percent of size of corpus

shuffle(posReviewSet)
shuffle(negReviewSet)

testSet = posReviewSet[:DIVISION_PROPORTION] + \
    negReviewSet[:DIVISION_PROPORTION]  # makes a test set that's 10 percent the size of the corpus
trainSet = posReviewSet[DIVISION_PROPORTION:] + \
    negReviewSet[DIVISION_PROPORTION:]  # makes a train set that's 90 percent the size of the corpus

referenceSets = collections.defaultdict(set)
testingSets = collections.defaultdict(set)

naiveBayesClassifier = NaiveBayesClassifier.train(trainSet)

for i, (features, name) in enumerate(testSet):
    referenceSets[name].add(i)
    observed = naiveBayesClassifier.classify(features)
    testingSets[observed].add(i)

ROUNDING_ACCURACY = 3
accVal = round(
    classify.accuracy(naiveBayesClassifier, testSet), ROUNDING_ACCURACY)
precisionVal = round(
    precision(referenceSets['pos'], testingSets['pos']), ROUNDING_ACCURACY)
recallVal = round(
    recall(referenceSets['pos'], testingSets['pos']), ROUNDING_ACCURACY)
fMeasureVal = round((2 * precisionVal * recallVal) /
                    (precisionVal + recallVal), ROUNDING_ACCURACY)

print("Info about this model:-")
print("\tAccuracy:", accVal)
print("\tPrecision:", precisionVal)
print("\tRecall:", recallVal)
print("\tF-Score:", fMeasureVal)

csvFields = [accVal, precisionVal, recallVal, fMeasureVal]
with open(RESULT_FILE_LOC, 'a', newline='') as resultsFile:
    writer = csv.writer(resultsFile)
    writer.writerow(csvFields)

resAnalyzer = ResultsAnalyser(RESULT_FILE_LOC)
stats = resAnalyzer.getAvgs()

print("Average (mean) findings from previous (and current) models:-")
print("\tAccuracy:", stats[0])
print("\tPrecision:", stats[1])
print("\tRecall:", stats[2])
print("\tF-Score:", stats[3])
