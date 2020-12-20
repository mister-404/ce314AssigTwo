# CE314 Assignment Two Report

### by bb18960

## Text Classification

This is aided heavily by a lot of nltk (natural language toolkit - found here: https://www.nltk.org/) functionality.





## Pre-processing

### Removal of common first names

Movie reviews may find it necessary to use an actor's first name. A name isn't usually a positive or negative thing and as such, it's not included in this modelling. I did this because I ran an early model and noticed that the word **elliot** was a common occurrence and I found that to be pretty unnecessary.

### Stop words

A stop word is a word that helps human readability and comprehension of a sentence but is realistically often exorbitant when it comes to natural language engineering. For example, a common stop word is **the**. The sentence "the girl walked merrily along" is pretty much just as useful in the problem we face on this assignment as "girl walked merrily along". One could even argue that along is excessive.



A problem that can arise when removing stop words is that you lose context that we might not find useful for the computer to eradicate such as the popular band: 'The Beatles' returning as Beatles instead. This sort of thing would likely not cause problems in this assignment.



We remove the stop words defined at nltk.corpus.stopwords.words('english').

### Punctuation and numbers

We also need to make sure that no punctuation slips through either. That's because tone/opinion is highly complex to gauge off of punctuation in computer programming.



The same could realistically be said for most numbers. A random number appearing in an article like 3 in: "The 3 candles burn all day" asks the question - how useful is that 3? I've made the executive decision to say that it isn't useful and so all numbers get removed except if they talk about a decade ie the 90s. This is because the 90s (for example) could have connotations of "cheesy" when it comes to movies. This might indicate a negative review and as such I find it relevant to stay.



## Feature Selection

I wanted to trawl the negative reviews and find what the essence of a negative review is and the same for positive. There are certain words that lend themselves to a particularly upbeat positive position such as "outstanding" and "groundbreaking" whereas we would expect to find negative reviews to be flavoured with "rubbish" and "abysmal". I decided to set out and find the most commonly occurring negative words.



## Evaluation

