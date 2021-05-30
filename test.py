import requests
import unittest

URL = "https://wholesomebot-api.herokuapp.com/"

class TestAPI(unittest.TestCase):

    def test_wholesomeBot_API(self):
        DATA = requests.get(url = URL)
        RESULT = "wholesomeBot API is working"
        self.assertEqual(DATA.json(), RESULT)
