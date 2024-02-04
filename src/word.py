import datetime
import random


thresholds = [
    [1, 1],
    [2, 5],
    [8, 10],
    [12, 16],
    [17, 20],
    [23, 28],
    [30, 38],
    [40, 50],
    [50, 60],
    [67, 80]
]


class Word:
    def __init__(self, foreign: str, english: str):
        self.foreign = [foreign]
        self.english = english
        self.current_cardbox = 0
        self.date_next_due = datetime.datetime.now().replace(hour=0, minute=0, second=0)

    def due(self):
        return self.date_next_due <= datetime.datetime.now()

    def add_foreign_translation(self, new):
        self.foreign.extend(new)

    def correct(self):
        if self.current_cardbox < 9:
            self.current_cardbox += 1
        self.date_next_due = (datetime.datetime.now() + datetime.timedelta(
            days=random.randint(
                thresholds[self.current_cardbox][0],
                thresholds[self.current_cardbox][1]
            )
        )).replace(hour=0, minute=0, second=0)

    def wrong(self):
        self.current_cardbox = 0
        self.date_next_due = (datetime.datetime.now() + datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0)

    def copy(self):
        a = Word("", "")
        a.foreign = self.foreign
        a.english = self.english
        a.current_cardbox = self.current_cardbox
        a.date_next_due = self.date_next_due
        return a

    def __repr__(self):
        return f"{self.english}: {self.foreign}, {self.due()}, {self.date_next_due}"


class WordBank:
    def __init__(self):
        self.words = {}

    def add_word(self, word):
        if word.english in self.words:
            self.words[word.english].add_foreign_translation(word.foreign)
        else:
            self.words[word.english] = word

    def update_word(self, old_translation, new_translation):
        old_word = self.words[old_translation].copy()
        old_word.english = new_translation
        self.words[new_translation] = old_word
        del self.words[old_translation]

    def get_word(self, english_word):
        return self.words[english_word]

    def delete_word(self, english_word):
        del self.words[english_word]

    def __iter__(self):
        self.__values = list(self.words.values())
        random.shuffle(self.__values)
        return iter(self.__values)

    def __add__(self, other):
        new_word_bank = WordBank()
        for i in self.words:
            new_word_bank.add_word(self.words[i])
        for i in other.words:
            new_word_bank.add_word(other.words[i])

        return new_word_bank

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return "\n".join([repr(i) for i in self.words.values()])


if __name__ == "__main__":  # to test word and word bank classes.
    a = WordBank()
    a.add_word(Word("f1", "e1"))
    a.add_word(Word("f2", "e2"))
    a.get_word("e2").add_foreign_translation("f3")
    for word in a:
        word.correct()

    print(a)