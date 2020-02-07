import json
from os import path

class FileHandler:

    @staticmethod
    def load_data(filepath, file_extension):
        if path.exists(filepath):
            with open(filepath, mode='r', encoding='utf-8') as data_file:
                thisdict = json.load(data_file)
            print("Dictionary loaded from " + filepath)
            return thisdict
        else:
            print(filepath + " does not exist.")

    @staticmethod
    def write_lines(filepath, lines):
        return "hi"
