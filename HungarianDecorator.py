"""
Module for decorating text with Hungarian notation.
"""
import nltk


class HungarianDecorator:
    def decorate_from_file(self, filename):
        pass

    def decorate_text(self, text):
        pass

    def decorate_sentence(self, sentence):
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        decorated_sentence = self.decorate_token(tagged)
        return decorated_sentence

    def decorate_token(self, token):
        decorated_token = []
        for word, tag in token:
            decorated_word = self.decorate_word(word)
            decorated_token.append(decorated_word)
        return decorated_token

    @staticmethod
    def decorate_word(word):
        return f"__{word}__"
        pass

    def decorate_punctuation(self, token):
        pass
