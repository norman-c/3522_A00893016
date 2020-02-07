from unittest import TestCase

from file_handler import FileHandler


class TestFileHandler(TestCase):
    def test_write_lines(self):
        line = "This is a test."
        FileHandler.write_lines("Test.txt", line)
        with open("Test.txt", "r") as data:
            content = data.read()
        self.assertEqual(content, line)
