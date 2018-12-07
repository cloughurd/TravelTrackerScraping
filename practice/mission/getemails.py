import time
from selenium import webdriver

starturl = "https://mail.aol.com/webmail-std/en-us/suite"

driver = webdriver.Chrome()
driver.get(starturl)
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="login-username"]').send_keys('jimclough1')

driver.find_element_by_xpath('//*[@id="login-signin"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys('L@uren01')

driver.find_element_by_xpath('//*[@id="login-signin"]').click()
time.sleep(7)
driver.find_element_by_xpath('//*[@id="dijit__Widget_1"]/div[8]/div[1]/div[8]').click()

driver.find_element_by_xpath('//*[@id="dojox_grid_Grid_0"]/div[1]/div/div/div/table/tbody/tr/th[7]').click()

//*[@id="page-0"]/div[1]
//*[@id="page-0"]/div[2]
//*[@id="page-0"]/div[25]

for x in range(25):
    