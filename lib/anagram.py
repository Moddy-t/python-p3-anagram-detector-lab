# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)
    
    def match(self, word_list):
        result = []
        for w in word_list:
            if sorted(w) == self.sorted_word:
                result.append(w)
        return result
