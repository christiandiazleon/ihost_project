# -*- coding: utf-8 -*-


# The setUp and tearDown methods run at the beginning and at the end of each
# test method (the ones that start with the word test).


from selenium import webdriver
import unittest


# creates a TestCase class
class NewVisitorTest(unittest.TestCase):

    # a setUp method that initializes the test. It opens the browser and
    # it waits for 3 seconds if needs to (if the page is not loaded).
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    # a tearDown method that runs after each test. It closes the browser.
    def tearDown(self):
        self.browser.quit()

    # a method that starts with test and that asserts that the title of the
    # webpage has Welcome to Django in it.
    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
