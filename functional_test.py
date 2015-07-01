from selenium import webdriver
import unittest

#Django receives the HTTp request, decides which view will handle it, view sends the response
class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser=webdriver.Firefox()
        self.browser.implicitly_wait(3)# selenium will work after 3 seconds of page loading

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Django',self.browser.title)
        self.fail('finsh the Test')

if __name__=='__main__':
    unittest.main(warnings='ignore')