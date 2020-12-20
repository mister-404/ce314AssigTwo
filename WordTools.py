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
