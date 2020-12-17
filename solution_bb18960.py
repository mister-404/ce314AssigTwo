'''
chapagain code found here http://blog.chapagain.com.np/python-nltk-sentiment-analysis-on-movie-reviews-natural-language-processing-nlp/?fbclid=IwAR3I2z_BbLSsLxK_qw8B-XTlRKBar2vzaAgd-0QPKUoWpjQTYD-m0a3kkT4
'''

from random import shuffle
from nltk.corpus import movie_reviews

documents = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        #documents.append((list(movie_reviews.words(fileid)), category))
        documents.append((movie_reviews.words(fileid), category))

print(len(documents))  # Output: 2000

# x = [str(item) for item in documents[0][0]]
# print (x)

# print first tuple
print(documents[0])
'''
Output:
 
(['plot', ':', 'two', 'teen', 'couples', 'go', ...], 'neg')
'''

# shuffle the document list
shuffle(documents)
