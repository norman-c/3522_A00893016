from file_handler import File_handler
class Dictionary:

    def __init__(self):
        self._dictionary = self.load_dictionary("data.json")
        self._loaded = True

    def load_dictionary(self, filepath):
        thisdict = File_handler.load_data(filepath, filepath)
        return thisdict

    def query_definition(self, word):
        return self._dictionary[word]

def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    dictionary = Dictionary()
    word = "Fishstix"
    print(dictionary.query_definition(word))


if __name__ == '__main__':
    main()