import unittest
from selenium import webdriver

class e2eTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"/Program Files/Google/Chrome/Application/chrome")
        self.driver.get("http://localhost:5000")

    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn("Named Entity", self.driver.title)