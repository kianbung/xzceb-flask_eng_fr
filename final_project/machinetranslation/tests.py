import unittest
from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    def test_en2fr(self):
        self.assertRegex(str(english_to_french('Hello')), 'Bonjour')
    def test_fr2en(self):
        self.assertRegex(str(french_to_english('Bonjour')), 'Hello')
    def test_en_null(self):
        self.assertIsNone(english_to_french(None))
    def test_fr_null(self):
        self.assertIsNone(french_to_english(None))



# execute
if __name__ == '__main__':
    unittest.main()