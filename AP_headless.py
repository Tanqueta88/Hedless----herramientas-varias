import unittest
from selenium import webdriver
from pageitems import PageItems
from selenium.webdriver.chrome.options import Options

class SearchCases(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument("headless")
        self.driver = webdriver.Chrome('/home/daniel/Escritorio/drivers/chromedriver', chrome_options=option)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        self.indexPage = PageIndex(self.driver)  # crea el objeto del tipo PageItems= indexPage
        self.itemsPage = PageItems(self.driver)
        #self.driver.maximize_window() #maximi ventana
        #self.driver.set_window_size(800, 600) #tamaño de ventana



    #@unittest.skip("Not needed now")
    def test_search_no_elements(self):
        self.indexPage.search('hola')
        self.assertEqual(self.itemsPage.return_no_element_text(), "No results were found for your search \"hola\"")

    #@unittest.skip("not needed now") #ignora este test
    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        self.assertTrue('DRESS' in self.itemsPage.return_section_title())

    def test_search_find_tshirts(self):
        self.indexPage.search('t-shirt')
        self.assertTrue('T-SHIRT' in self.itemsPage.return_section_title())

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
