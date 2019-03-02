# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ddt import ddt, data, unpack
import csv


import unittest
#import test_data
import time


class BasePage (object):
    """klasa bazowa"""

    def __init__(self,driver):
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        return
