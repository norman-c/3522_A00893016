import json
from os import path

class File_handler:

    @staticmethod
    def load_data(filepath, file_extension):
        if(path.exists(filepath)):
            with open(filepath) as f_in:
                thisdict = json.load(f_in)
            print("Dictionary loaded from " + filepath)
            return thisdict
        else:
            print(filepath + " does not exist.")

    @staticmethod
    def write_lines(filepath, lines):
        return "hi"
