## Introduction
Welcome to the second tutorial in this course! Like always, my goal today is to blow your minds - this time with a fancy little thing called Natural Language Processing. Natural Language Processing, or NLP is essentially a methodology for analyzing, understanding, and giving context to groupings of words progromatically. It's extremely powerful, only growing in use, and today, you're going to learn how to use it!

In order to learn about NLP, we're going to build a speech analyzer, that will allow its users to input a speech of their choice, and then figure out if that speech aligns more with one oppinion, or another. Here's how it will work:
1) The user gives us three speeches - The first speech will be in support of an idea, the second speech will be in opposition to an idea, and the last speech will be compared to the previous two speeches to figure out if the person giving that third speech is in support or opposition to an idea.
2) We take all three speeches, and use NLP to remove unimportant words (Like 'is' and 'and'), and then we figure out the words that are most commonly used in the opposition and support speech, as well as in the speech that we're checking
3) We figure out if the wording used in the speech to check is more similar to the speech that's in support or opposition, and then tell our user how that speech aligns

## Installing Dependencies
Before we can start using natural language processing, we must first import the requisite packages. Begin by heading over to replt.it, creating a Python REPL, and importing the following packages

```python
import spacy
import json
import string
from collections import Counter
```

## Basic Setup
The first thing you all need to understand about NLP, is the fundamental manner in which it functions. Simply put, Natural Language Processing starts by dividing up sentences into bunches of tokens that seperate individual words and punctuation. Then NLP santizes sentences by removing 'stop words' (words like 'for', 'and', 'but', etc.), and lemmatizes words into their simplest forms (e.g. running becomes run, swimming becomes swim). Lemmatization is especially crucial because it allows us to compare words with nearly identical meanings, even if those words' forms are different. 

To begin, let's find the three speeches that we want to use for our project. Feel free to copy my speeches below, but if you want to find your own, make sure that they encompass the whole issue - meaning that they don't make one argument but the entire argument.

```python
proSpeech = ''
antiSpeech = ''
checkSpeech = ''
```

## Pure Craziness - Using Machine Learning to Gauge the Sentiment of a tweet!!
Allright guys, ****'s about to get crazy!! I don't expect any of you to understand what this code is saying. I don't even expect you to understand what's it's doing. All I want you guys to realize is that we're literally using machine learning to gauge the sentiment of a tweet - and we're only using 100 lines of code!! To start, open up a new Python REPL

In the main.py file:
```python
import nltk
```

Press run. Then after your code finishes running, execute the following lines in the Bash console:
```bash
nltk.download('twitter_samples')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
```

Next, clear both the main.py file, and the bash console. Paste the following lines of code into your main.py file, and press run:

```python
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier

import re, string, random

def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token

def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)

if __name__ == "__main__":

    positive_tweets = twitter_samples.strings('positive_tweets.json')
    negative_tweets = twitter_samples.strings('negative_tweets.json')
    text = twitter_samples.strings('tweets.20150430-223406.json')
    tweet_tokens = twitter_samples.tokenized('positive_tweets.json')[0]

    stop_words = stopwords.words('english')

    positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
    negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

    positive_cleaned_tokens_list = []
    negative_cleaned_tokens_list = []

    for tokens in positive_tweet_tokens:
        positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    for tokens in negative_tweet_tokens:
        negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    all_pos_words = get_all_words(positive_cleaned_tokens_list)

    freq_dist_pos = FreqDist(all_pos_words)
    print(freq_dist_pos.most_common(10))

    positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
    negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)

    positive_dataset = [(tweet_dict, "Positive")
                         for tweet_dict in positive_tokens_for_model]

    negative_dataset = [(tweet_dict, "Negative")
                         for tweet_dict in negative_tokens_for_model]

    dataset = positive_dataset + negative_dataset

    random.shuffle(dataset)

    train_data = dataset[:7000]
    test_data = dataset[7000:]

    classifier = NaiveBayesClassifier.train(train_data)

    print("Accuracy is:", classify.accuracy(classifier, test_data))

    print(classifier.show_most_informative_features(10))

    custom_tweet = "I ordered just once from TerribleCo, they screwed up, never used the app again."

    custom_tokens = remove_noise(word_tokenize(custom_tweet))

    print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
```

Don't worry if it takes forever for your code to run - expect to wait at least 1-2 minutes while the machine learning model trains itself. In the meantime, prepare to have your mind blown!!

## Last Thoughts
Natural language processing is one of the many powerful technologies that will become a staple of the 21st century. I hope that we've done today will inspire you to continue learning to code, and finding more crazy things to build!
