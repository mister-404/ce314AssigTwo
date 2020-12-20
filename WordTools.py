'''
Provides tooling for the different word associated
tasks that need to be carried out in this project

bb18960
'''

from nltk.corpus import stopwords, movie_reviews
from nltk import ngrams
import re
from CommonNamesFinder import CommonNamesFinder

NAMES = CommonNamesFinder().names
ENGLISH_STOPWORDS = stopwords.words('english')


class WordTools:
    @classmethod
    def bothBags(cls, words):
        normalBag = WordTools.bagOfWords(words)
        biBag = WordTools.biBagOfWords(words)
        bothFeatures = normalBag.copy()
        bothFeatures.update(biBag)
        return bothFeatures

    @classmethod
    def bagOfWords(cls, words):
        return dict((word, True) for word in WordTools.removeUneeded(words))

    @classmethod
    def biBagOfWords(cls, words, wordGroupSize=2):
        cleanedWords = WordTools.removeUneeded(words, stopWords=[])
        wordArr = [wordGrouping for wordGrouping in iter(
            ngrams(cleanedWords, wordGroupSize))]

        return dict((wordGroup, True) for wordGroup in wordArr)

    @classmethod
    def getReviews(cls, reviewOpinion):
        return [movie_reviews.words(fileid) for fileid in movie_reviews.fileids(reviewOpinion)]

    @classmethod
    def removeUneeded(cls, words, stopWords=ENGLISH_STOPWORDS):
        cleanedWords = []
        for word in words:
            isAStopWord = word in stopWords
            justPunctuation = re.sub(r"^(\W+|\d+)$", "", word) == ""
            isAName = word in NAMES

            if not(justPunctuation or isAStopWord or isAName):
                cleanedWords.append(word.lower())
        return cleanedWords
