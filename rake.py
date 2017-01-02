"""RAKE Algorithm Implementation"""
import re

from utils import process_string, split_words
from settings import STOPWORDS_LIST


class Rake(object):
    """Main Rake algorithm class"""

    def __init__(self, text=str(), *args, **kwargs):
        super(Rake, self).__init__(*args, **kwargs)
        if text:
            self.text = process_string(text)
        else:
            raise ValueError("Text is empty.")

    def stopwords(self):
        """Return a list of stopwords."""
        with open(STOPWORDS_LIST, 'r') as content:
            return content.read().splitlines()

    def stopwords_regex(self):
        """Return a list of stopwords regexes."""
        regexes = list()
        for stopword in self.stopwords():
            regexes.append(r'\b' + stopword + r'\b')
        return re.compile('|'.join(regexes), re.IGNORECASE)

    def sentences(self):
        """Return a list of sentences extracted text."""
        return re.compile(r'[.!?;:,\t\(\)\"\']|\s-\s').split(self.text)

    def candidate_keywords(self):
        """Return a list of candidate phrases after removing stopwords."""
        candidate_phrases = list()
        for sentence in self.sentences():
            candidate_sentence = re.sub(self.stopwords_regex(), '|', sentence)
            phrases = candidate_sentence.split("|")
            for phrase in phrases:
                phrase = process_string(phrase).lower()
                if phrase:
                    candidate_phrases.append(phrase)
        return candidate_phrases

    def word_scores(self):
        """Return score of each word using the formula: deg(w)/freq(w)"""
        word_degree = dict()
        word_frequency = dict()
        for phrase in self.candidate_keywords():
            degree = len(phrase) - 1
            words = split_words(phrase)
            for word in words:
                word_frequency[word] = word_frequency.get(word, 0) + 1
                word_degree[word] = word_degree.get(word, 0) + degree
        for word in word_frequency:
            word_degree[word] = word_degree[word] + word_frequency[word]
        # word score is degree(word) / frequency(word)
        word_scores = dict()
        for word in word_frequency:
            word_scores[word] = word_degree[word] / word_frequency[word]
        return word_scores

    def phrase_scores(self):
        """Return score of each phrase by calculating word scores."""
        phrase_scores = dict()
        word_scores = self.word_scores()
        for phrase in self.candidate_keywords():
            words = split_words(phrase)
            for word in words:
                phrase_scores[phrase] = phrase_scores.get(phrase, 0) + word_scores[word]
        return phrase_scores
