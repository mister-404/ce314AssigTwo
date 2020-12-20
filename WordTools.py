from nltk.corpus import stopwords, movie_reviews
import re
from CommonNamesFinder import CommonNamesFinder

NAMES = CommonNamesFinder().names
ENGLISH_STOPWORDS = stopwords.words('english')


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
        for word in words:
            isAStopWord = word in ENGLISH_STOPWORDS
            justPunctuation = re.sub(r"^(\W+|\d+)$", "", word) == ""
            isAName = word in NAMES

            if not(justPunctuation or isAStopWord or isAName):
                cleanedWords.append(word)
        return cleanedWords
