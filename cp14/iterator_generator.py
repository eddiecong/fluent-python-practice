import re
import reprlib
from typing import Sequence, Text

RE_WORD = re.compile('\w+')


class SentenceLoader:
    """
    SentenceLoader object is iterable thanks to the __getitem__ function, 
    which will loop over the words in sequence.
    """
    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORD.findall(self.text)
    
    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)


class Sentence:
    """
    Sentence object holds the internal state of attributes text and
    return the sentenceIterator object to make itself iterable.
    """
    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORD.findall(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)

    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)


class SentenceIterator:
    """
    Iterator class: also iterable 
    manuplate the words of Sentence object, could be polymorphic.
    """
    def __init__(self, words) -> None:
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration("out of index.")
        self.index += 1
        return word

    def __iter__(self):
        return self


class SentenceGenerator:
    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORD.findall(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
    
    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)


if __name__ == "__main__":
    text = '"These days, Hong Kong is rainy and wet."'
    s = SentenceLoader(text=text)
    s_iterator1 = iter(s)
    print(s_iterator1)
    print(s[0])
    s = Sentence(text=text)
    s_iterator2 = iter(s)
    print(s_iterator2)
    for i in s_iterator2:
        print(i)

    s_generator = SentenceGenerator(text=text)
    for i in s_generator:
        print(i)
