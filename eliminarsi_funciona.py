'''import unittest #libreria que ejecuta las pruebas propiamente dichas
from selenium import webdriver
import time

class SearchCases(unittest.TestCase): #las clases se definen con la palabra reservada CLASS

    def setUp(self): #METODO SUTUP:se ejecuta antes de cada prueba (Precondicion)
        self.driver = webdriver.Chrome('/home/daniel/workspaces/fogar-testing/Automation - Clases/chromedriver'
        self.driver.get('http://automationpractice.com/index.php')
        time.sleep(5)


        def tearDown(self):
            self.driver.close()
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()'''''

import unittest
from selenium import webdriver
import time

class SearchCases(unittest.TestCase):

    def test_search_no_elements(self):
        self.driver = webdriver.Chrome('/home/daniel/Escritorio/drivers/chromedriver')
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.find_element_by_id('search_query_top').send_keys('hola')
        self.driver.find_element_by_name('submit_search').click()
        time.sleep(2)
        #result = driver.find_element_by_xpath('//*[@id="center_column"]/p').text
        #expected_result = 'No results were found for your search "hola"'
        self.assertEqual(driver.find_element_by_xpath('//*[@id="center_column"]/p').text, 'No results were found for your search "hola"')
        driver.close()
        driver.quit()

    def test_search_find_dresses(self):
        driver = webdriver.Chrome('Chromedriver.exe')
        driver.get('http://automationpractice.com/index.php')
        driver.find_element_by_id('search_query_top').send_keys('dress')
        driver.find_element_by_name('submit_search').click()
        time.sleep(2)
        #result = driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text
        #expected_result = 'DRESS'
        self.assertTrue('DRESS' in driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text)
        driver.close()
        driver.quit()


if __name__ == '__main__':
    unittest.main()