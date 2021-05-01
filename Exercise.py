from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

base_url = "http://automationpractice.com/index.php"

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(base_url)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

class Search(BaseTest):
    def test_isExist(self):

        # Search Item
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "search_query_top"))).send_keys("blouse")

        # Click Search Button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "submit_search"))).click()

        # Verify
        # actual_text = self.driver.find_element_by_class_name("heading-counter").text
        # self.assertEqual("1 result has been found.", actual_text)

        actual_text = self.driver.find_element_by_xpath('//*[@id="center_column"]/ul/li/div/div[2]/h5/a').text
        self.assertEqual("Blouse", actual_text)

    def test_notExist(self):
        # Search Item
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "search_query_top"))).send_keys("outwear")

        # Click Search Button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "submit_search"))).click()

        # Verify
        actual_text = self.driver.find_element_by_class_name("heading-counter").text
        self.assertEqual("0 results have been found.", actual_text)

        # actual_text = self.driver.find_element_by_xpath('//*[@id="center_column"]/p').text
        # self.assertEqual("No results were found for your search outwear", actual_text)