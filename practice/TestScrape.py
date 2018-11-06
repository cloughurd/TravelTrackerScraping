import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException

templeListUrl = "https://www.lds.org/temples/list"
coordinateGetterUrl = "https://www.gps-coordinates.net/"

driver = webdriver.Chrome()
driver.get(templeListUrl)

temples = []

for x in range(190):
    try:
        temple = driver.find_element_by_xpath('//*[@id="app"]/div/main/section/div[3]/div[2]/li[' + str(x+1) + ']/a/span')
        temples.append(temple.text.encode('ascii', 'ignore'))
    except NoSuchElementException:
        try:
            temple = driver.find_element_by_xpath('//*[@id="app"]/div/main/section/div[3]/div[2]/li[' + str(x+1) + ']/span[1]')
            temples.append(temple.text.encode('ascii', 'ignore'))
        except NoSuchElementException:
            print("***Couldn't find that one :/")
# print(temples)

driver.get(coordinateGetterUrl)
time.sleep(5)

templeCoordinateMap = {}

for temple in temples:
    # print(temple)
    try:
        search = driver.find_element_by_xpath('//*[@id="address"]')
        search.clear()
        search.send_keys(temple)
        button = driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[3]/div[1]/form[1]/div[2]/div/button')
        button.click()
        time.sleep(2)
        latitude = driver.find_element_by_xpath('//*[@id="latitude"]')
        longitude = driver.find_element_by_xpath('//*[@id="longitude"]')
        templeCoordinateMap[temple] = (latitude.get_attribute('value').encode('ascii', 'ignore'), longitude.get_attribute('value').encode('ascii', 'ignore'))
        print(templeCoordinateMap[temple])
    except UnexpectedAlertPresentException:
        alert = driver.switch_to_alert()
        alert.accept()
        print("***Couldn't find that one on the map")
    except Exception:
        print(temple)
    time.sleep(1)
print(templeCoordinateMap)
print(len(templeCoordinateMap))
driver.quit()
# //*[@id="app"]/div/main/section/div[3]/div[2]/li[2]/span[1]
# //*[@id="app"]/div/main/section/div[3]/div[2]/li[190]/a/span
# testPage = requests.get('https://www.lds.org/temples/list')

# soup = BeautifulSoup(testPage.content, 'html.parser')

# results = soup.findAll("li", "filterResult-1Hx44")
# print(results)
