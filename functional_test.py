from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest,time

#Django receives the HTTp request, decides which view will handle it, view sends the response
class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser=webdriver.Firefox()
        self.browser.implicitly_wait(3)# selenium will work after 3 seconds of page loading

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-do',self.browser.title)

        header_text=self.browser.find_element_by_tag_name('h1').text # get inside text of <h1>
        self.assertIn('To-do',header_text)

        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        inputbox.send_keys('Buy peacock feathers') # this will type automatiaclly into inputbox
        inputbox.send_keys(Keys.ENTER)

        table= self.browser.find_element_by_id('id_list_table')
        rows=[table.find_element_by_tag_name('tr')]
        self.assertIn('1: Buy peacock feathers',[row.text for row in rows])
        #self.fail('finsh the Test')
    

if __name__=='__main__':
    unittest.main(warnings='ignore')