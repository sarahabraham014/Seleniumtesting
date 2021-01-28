from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

email = 'test@gmail.com'
password ='123456'
url = 'https://nodauth.herokuapp.com/'


# /html/body/div[1]/div/div/a[2]

driver = webdriver.Chrome('./chromedriver') 
driver.get(url)
driver.find_element_by_xpath('/html/body/div[1]/div/div/a[2]').click()

em =driver.find_element_by_xpath('//*[@id="email"]')
em.clear()
em.send_keys(email)
ps =driver.find_element_by_xpath('//*[@id="password"]')
ps.clear()
ps.send_keys(password)

# /html/body/div/div[1]/div/form/button

driver.find_element_by_xpath('/html/body/div/div[1]/div/form/button').click()


print(driver.find_element_by_xpath('/html/body/p').text)
