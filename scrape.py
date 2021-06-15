from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

url = 'https://the-internet.herokuapp.com/login'

driver.get(url)

driver.find_element_by_xpath('//*[@id="username"]').send_keys('tomsmith')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('SuperSecretPassword!')

driver.find_element_by_xpath('//*[@id="login"]/button').click()

driver.quit()
