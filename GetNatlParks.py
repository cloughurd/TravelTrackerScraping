from selenium import webdriver
import traceback
from selenium.common.exceptions import NoSuchElementException

url = "https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

outputFile = open("NationalParks.json", "w+")
outputFile.write("[\n")

for x in range(60):
    try:
        name = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(x+1) + ']/th/a')
    except NoSuchElementException:
        try:
            name = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(x+1) + ']/td[1]/a')
        except Exception:
            driver.quit()
            traceback.print_exc()
            break
    try:
        coord = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(x+1) + ']/td[2]/small/span/span/a/span[3]/span/span[1]')
    except NoSuchElementException:
        try:
            coord = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(x+1) + ']/td[3]/small/span/span/a/span[3]/span/span[1]')
        except Exception:
            driver.quit()
            traceback.print_exc()
            break
    nameString = name.get_attribute('title').encode('ascii', 'ignore')
    coordString = coord.text.encode('ascii', 'ignore')
    latitude = coordString.split()[0]
    longitude = coordString.split()[1]
    latLen = len(latitude)
    longLen = len(longitude)
    if(latitude[latLen-1:] == "S"):
        latitude = "-" + latitude
        latLen += 1
    latitude = latitude[0:latLen -1]
    if(longitude[longLen-1:] == "W"):
        longitude = "-" + longitude
        longLen += 1
    longitude = longitude[0:longLen-1]
    print(nameString, latitude, longitude)
    outputFile.write('{"label":"' + nameString + '", "latitude":"' + latitude + '", "longitude":"' + longitude + '" }')
    if(x < 59):
        outputFile.write(',\n')
    # except Exception:
    #     driver.quit()
    #     traceback.print_exc()
    #     break
outputFile.write("\n]")
driver.quit()
