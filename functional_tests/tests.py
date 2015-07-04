from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
import unittest
import time


# Django receives the HTTp request, decides which view will handle it,


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # selenium will work after 3 seconds of page loading
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = [table.find_element_by_tag_name('tr')]
        for row in rows:
            print("content: %s" % row.text)
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)
        self.assertIn('To-do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name(
            'h1').text  # get inside text of <h1>
        self.assertIn('To-do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # this will type automatiaclly into inputbox
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('play cricket')
        inputbox.send_keys(Keys.ENTER)

        # self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table(
            '2: play cricket')

        self.fail('finsh the Test')
