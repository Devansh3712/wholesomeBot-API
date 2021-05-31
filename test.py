import requests
import unittest

URL = "https://wholesomebot-api.herokuapp.com"

class TestAPI(unittest.TestCase):

    def test_wholesomeBot_API(self):
        DATA = requests.get(url = URL)
        RESULT = "wholesomeBot API is working"
        self.assertEqual(DATA.json(), RESULT)

    def test_info(self):
        DATA = requests.get(url = f"{URL}/info")
        RESULT = "https://github.com/Devansh3712"
        self.assertEqual(DATA.json()["GitHub"], RESULT)
