from unittest import TestCase

from dictionary import Dictionary


class TestDictionary(TestCase):
    def test_load_dictionary(self):
        this_dict = Dictionary()
        self.assertTrue(this_dict._loaded)

    def test_query_definition(self):
        this_dict = Dictionary()
        define = ["Site that cannot be used for any purpose, being contaminated by pollutants."]
        self.assertTrue(this_dict.query_definition("abandoned industrial SITE") == define)
