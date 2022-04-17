import unittest
from translator import englishToFrench, frenchToEnglish


class TestTranslator(unittest.TestCase):
    def test_en2fr(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertIsNotNone(english_to_french(None))
    def test_fr2en(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertIsNotNone(french_to_english(None))

# execute
if __name__ == '__main__':
    unittest.main()