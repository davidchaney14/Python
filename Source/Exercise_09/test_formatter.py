import unittest, formater 

class TestFormatter(unittest.TestCase):
    def test_lower(self):
        test_text = "DAVID CHANEY"
        result = formater.convert_lower(test_text)
        self.assertEqual(result, "david chaney")

    def test_upper(self):
        test_text = "David Chaney"
        result = formater.convert_upper(test_text)
        self.assertEqual(result, "DaVID CHANEY")

if __name__ == "__main__":
    unittest.main()
