from file_handler import FileHandler, InvalidFileTypeError


class Dictionary:

    def __init__(self):
        self._dictionary = self.load_dictionary("data.json")
        self._loaded = True

    def load_dictionary(self, filepath):
        thisdict = FileHandler.load_data(filepath, filepath)
        return thisdict

    def query_definition(self, word):
        for key in self._dictionary:
            if key.lower() == word.lower():
                return self._dictionary[key]
        raise KeyError


def main():
    definition = ""
    write_path = "queries.txt"
    word = "orange"
    try:
        print("\nDictionary Program")
        print("-----------------------")
        print("Loading dictionary")
        dictionary = Dictionary()
        user_input = None
        while user_input != "exitprogram":
            print("Enter exitprogram to exit program.")
            string_input = input("Enter word to look up:")

            # handle user pressing only enter in menu
            if (string_input == ''):
                continue

            user_input = string_input

            if user_input == "exitprogram":
                pass
            else:
                try:
                    define = dictionary.query_definition(user_input)
                    definition = definition.join(define)
                    line = user_input.title() + ": " + definition + "\n"
                    print(line)
                    FileHandler.write_lines(write_path, line)
                    print("Query written to " + write_path + ".\n")
                except KeyError:
                    print(word + " not found in dictionary.\n")
    except InvalidFileTypeError:
        print("File not found.")
    finally:
        print("Exiting program.")



if __name__ == '__main__':
    main()
