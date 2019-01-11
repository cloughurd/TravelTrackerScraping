import json
import sys
import pickle

inputFileName = "OutputCoordinates.txt"
outputFileName = "JSONCleaned.json"

if(len(sys.argv) > 1):
	inputFileName = sys.argv[1]
	outputFileName = "Cleaned" + sys.argv[1]
if(len(sys.argv) > 2):
	inputFileName = sys.argv[1]
	outputFileName = sys.argv[2]

inputFile = open(inputFileName, "r")
dict = pickle.load(inputFile)
dictSize = len(dict)
itemNum = 0

outputFile = open(outputFileName, "w+")

outputFile.write("[\n")
for key, value in dict.items():
	outputFile.write('{"label":"' + key + '", "latitude":"' + value[0] + '", "longitude":"' + value[1] + '" }')
	if(itemNum < dictSize - 1):
		outputFile.write(",")
	outputFile.write("\n")
	itemNum += 1

outputFile.write("]")
