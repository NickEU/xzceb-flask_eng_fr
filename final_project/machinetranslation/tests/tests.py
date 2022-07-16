import unittest

import sys
sys.path.insert(0,'..')

from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_englishToFrench_translation(self):
        self.assertEqual('Bonjour', englishToFrench('Hello'))
    def test_frenchToEnglish_translation(self):
        self.assertEqual('Hello', frenchToEnglish('Bonjour'))
    def test_englishToFrench_null_input(self):
        self.assertEqual(None, englishToFrench(None))
    def test_frenchToEnglish_null_input(self):
        self.assertEqual(None, frenchToEnglish(None))

if __name__ == '__main__':
    unittest.main()
