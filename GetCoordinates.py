import sys
import time
import pickle
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException

# Setup default file names for input and output
inputFileName = "InputCoordinates.txt"
outputFileName = "OutputCoordinates.txt"

# Check for optional arguments for input and output file names
if(len(sys.argv) > 2):
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
if(len(sys.argv) > 1):
    inputFileName = sys.argv[1]
    outputFileName = "Coordinates" + sys.argv[1]

# Initialize coordinate search URL
coordinateGetterUrl = "https://www.gps-coordinates.net/"

# Initialize web driver to that URL
driver = webdriver.Chrome()
driver.get(coordinateGetterUrl)
driver.maximize_window()
time.sleep(3)

# Initialize containers
resultsMap = {}
inputList = []

# Import input from file
inputFile = open(inputFileName, "r")
inputList = pickle.load(inputFile)

# Iterate through input and get coordinates
for item in inputList:
    try:
        search = driver.find_element_by_xpath('//*[@id="address"]')
        search.clear()
        search.send_keys(item)
        button = driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[3]/div[1]/form[1]/div[2]/div/button')
        button.click()
        time.sleep(1)
        latitude = driver.find_element_by_xpath('//*[@id="latitude"]')
        longitude = driver.find_element_by_xpath('//*[@id="longitude"]')
        resultsMap[item] = (latitude.get_attribute('value').encode('ascii', 'ignore'), longitude.get_attribute('value').encode('ascii', 'ignore'))
    except UnexpectedAlertPresentException:
        alert = driver.switch_to_alert()
        alert.accept()
        with open("log.txt", "a") as errorLog:
            errorLog.write("WARNING in " + sys.argv[0] + " with " + item + ": couldn't find\n")
    except Exception:
        with open("log.txt", "a") as errorLog:
            errorLog.write("ERROR in " + sys.argv[0] + " with " + item + ": unknown exception\n")
    time.sleep(.5)

# Close the driver
driver.quit()

# Export result to output file
outputFile = open(outputFileName, "w")
print(outputFileName)
pickle.dump(resultsMap, outputFile)
