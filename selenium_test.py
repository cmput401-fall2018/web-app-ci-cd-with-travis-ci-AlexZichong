from selenium import webdriver

from selenium.webdriver.common.keys import Keys

def test_home():

    driver = webdriver.Chrome("chromedriver")

    #link = "https://accounts.google.com"
    #driver = webdriver.Chrome(executable_path='chromedriver')
    #driver.get(link)

   
    driver.get("http://199.116.235.96:8000")

    elem = driver.find_element_by_id("name")

    assert elem != None