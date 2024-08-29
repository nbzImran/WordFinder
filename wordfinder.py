"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    
    """test for finding words from a file.


    >>> wf = WordFinder('word2.txt')

    >>> wf.get_random_word() in ['cat', 'dog', 'rat']
    True

    >>> wf.get_random_word() in ['cat', 'dog', 'rat']
    True

    """
    

    def __init__(self, path):
                file_path = open(path)
                self.word = self.get_load_word(file_path)


    def  get_load_word(self, file_path):
            return [w.strip() for w in file_path] 


    def get_random_word(self):
            if not self.word:
                    raise ValueError("word is either empty line or commen")
            return random.choice(self.word)
    

    # def print_word(self):
    #         for word in self.word:
    #                 print(word)



class supper_WF(WordFinder):
    """
    random word if word not start with space or #.

    >>> swf = supper_WF('complex.txt')


    swf.get_random_word() in ['shyton', 'Iblis', 'poppy', 'human']
    True
    """


    def get_load_word(self, file_path):
           return [w.strip() for w in file_path
                   if w.strip() and not w.startswith("#")]


