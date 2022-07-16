""" Unit tests for translator """
import unittest

import sys

sys.path.insert(0, '..')

from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    """ Unit tests for translator """
    def test_english_to_french_translation(self):
        """ Test the translation of text from English to French """
        self.assertEqual('Bonjour', english_to_french('Hello'))

    def test_french_to_english_translation(self):
        """ Test the translation of text from French to English """
        self.assertEqual('Hello', french_to_english('Bonjour'))

    def test_english_to_french_null_input(self):
        """ Tests that English to French handles null values properly """
        self.assertEqual(None, english_to_french(None))

    def test_french_to_english_null_input(self):
        """ Tests that French to English handles null values properly """
        self.assertEqual(None, french_to_english(None))


if __name__ == '__main__':
    unittest.main()
