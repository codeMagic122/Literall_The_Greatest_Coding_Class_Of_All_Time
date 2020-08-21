## Introduction
Welcome to the second tutorial in this course! Like always, my goal today is to blow your minds - this time with a fancy little thing called Natural Language Processing. Natural Language Processing, or NLP is essentially a methodology for analyzing, understanding, and giving context to groupings of words progromatically. It's extremely powerful, only growing in use, and today, you're going to learn how to use it!

## Project Setup
Like last time, we're goint to start by creating a new Python REPL on REPL.it. Next, we're going to download some data from a package called nltk (Natural Language Processing Toolkit):

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