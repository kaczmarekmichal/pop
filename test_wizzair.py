# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage


import unittest
#import test_data
import time


class WizzairRegistation(unittest.TestCase):

    def setUp(self):
        self.driver= webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl/main-page#/")


    def tearDown(self):
        self.driver.quit

    def test_correct_registation(self):
        home_page = HomePage(self.driver)
        home_page.click_zaloguj_button()

if __name__== '__main__':
    unittest.main(verbosity=2)
