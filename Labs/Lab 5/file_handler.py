import json
from os import path

from file_extensions import FileExtensions


class FileHandler:

    @staticmethod
    def load_data(filepath, file_extension):
        try:
            if FileExtensions.json.name in filepath or FileExtensions.txt.name in filepath:
                with open(filepath, mode='r', encoding='utf-8') as data_file:
                    this_dict = json.load(data_file)
                return this_dict
            raise FileNotFoundError
        except FileNotFoundError:
            raise InvalidFileTypeError

    @staticmethod
    def write_lines(filepath, lines):
        if path.exists(filepath):
            with open(filepath, "a") as text_file:
                text_file.write(lines)
        else:
            with open(filepath, "w") as text_file:
                text_file.write(lines)


class InvalidFileTypeError(Exception):

    def __init__(self):
        pass
