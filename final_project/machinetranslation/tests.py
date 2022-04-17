import unittest
from translator import englishToFrench, frenchToEnglish


class TestTranslator(unittest.TestCase):
    def test_en2fr(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertIsNotNone(englishToFrench(None))
    def test_fr2en(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertIsNotNone(frenchToEnglish(None))

# execute
if __name__ == '__main__':
    unittest.main()