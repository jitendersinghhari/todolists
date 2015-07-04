from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

# Django receives the HTTp request, decides which view will handle it, view sends the response


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)  # selenium will work after 3 seconds of page loading

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = [table.find_element_by_tag_name('tr')]
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text  # get inside text of <h1>
        self.assertIn('To-do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        inputbox.send_keys('Buy peacock feathers')  # this will type automatiaclly into inputbox
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        time.sleep(10)

        # self.fail('finsh the Test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
