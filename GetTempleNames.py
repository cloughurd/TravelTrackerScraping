import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pickle

# Set default number of temples
numTemples = 190

# Read in optional argument for different number of temples
if(len(sys.argv) > 1):
    numTemples = int(sys.argv[1])

# Set URL to site with list of temples
templeListUrl = "https://www.lds.org/temples/list"

# Initialize web driver to that URL
driver = webdriver.Chrome()
driver.get(templeListUrl)

# Initialize list to put temple names into
templeNames = []

for x in range(numTemples):
    try:
        # First looks for temple name within the hyperlink
        temple = driver.find_element_by_xpath('//*[@id="app"]/div/main/section/div[3]/div[2]/li[' + str(x+1) + ']/a/span')
	templeLoc = driver.find_element_by_xpath('//*[@id="app"]/div/main/section/div[3]/div[2]/li[' + str(x+1) + ']/span[1]')
	if u"Location" not in templeLoc.text:
            templeNames.append(temple.text.encode('ascii', 'ignore'))
    except NoSuchElementException:
        try:
            # If it isn't a link, try the bare text way
            temple = driver.find_element_by_xpath('//*[@id="app"]/div/main/section/div[3]/div[2]/li[' + str(x+1) + ']/span[1]')
	    templeLoc = driver.find_element_by_xpath('//*[@id="app"]/div/main/section/div[3]/div[2]/li[' + str(x+1) + ']/span[2]')
            if u"Location" not in templeLoc.text:
		templeNames.append(temple.text.encode('ascii', 'ignore'))
        except NoSuchElementException:
            with open("log.txt", "a") as errorLog:
                errorLog.write("ERROR in " + sys.argv[0] + " on " + str(x) + "\n")

# Close the driver
driver.quit()

# Open and write temple names to file
fileName = "TempleNamesList.txt"
templeFile = open(fileName, "w")
print(fileName)
pickle.dump(templeNames, templeFile)
