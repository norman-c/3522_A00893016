"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""
import cProfile
import string


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    COMMON_PUNCTUATION = ",*;.:([])"

    def __init__(self):
        self.text = None

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # read lines
        with open(src, mode='r', encoding='utf-8') as book_file:
            self.text = book_file.readlines()

        # strip out empty lines
        stripped_text = []
        for line in self.text:
            if line != "\n":
                stripped_text.append(line.lower())
        self.text = stripped_text

        # convert list of lines to list of words
        words = []
        for line in self.text:
            words += line.split()
        self.text = words

        temp_text = []
        for word in self.text:
            temp_word = word
            temp_word = temp_word.translate(str.maketrans('', '', self.COMMON_PUNCTUATION))
            temp_text.append(temp_word)
        self.text = set(temp_text)
        return self.text
 


def main():
    book_analyzer = BookAnalyzer()
    unique_words = book_analyzer.read_data()
    print("-" * 50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-" * 50)
    count = 0
    for word in unique_words:
        print(word)
    print("-" * 50)
    print(len(unique_words))


if __name__ == '__main__':
    main()
