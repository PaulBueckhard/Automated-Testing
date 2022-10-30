import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class e2eTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'/webdrivers/chromedriver')
        self.driver.get("http://localhost:5000")

    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn("Named Entity", self.driver.title)

    def test_page_heading_is_named_entity_finder(self):
        heading = self._find("heading").text
        self.assertEqual("Named Entity Finder", heading)

    def _find(self, val):
        return self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{val}"]')