#Import a json dataset from a URL, and save it as a LIST. 
#Saving in a LIST format is easier to deal with the file and to the search of regular expressions

import json
import pandas as pd
import datetime
import re
import sys
import numpy as np

# import urllib library
import urllib

#Importing the Json format dataset from web
url = "https://data.cityofnewyork.us/resource/pvqr-7yc4.json?$limit=1000000"

  
# store the response of URL
response = urllib.urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())

#-------------------------------------------------------------------------------------
#Saving the json file from URL as a list in a TXT FILE. Its easier to deal with different lines and data when converting to list
mapped_vals = []
for ent in data_json:
    mapped_vals.append(ent)

textfile = open("ny_transit.txt", "w") #creating a new file called ny_transit
for element in mapped_vals:
    textfile.write(str(element)+ "\n") 
textfile.close()

#Saving the Json file in directory
with open('pvqr-7yc4.json', 'w') as json_file:
    json.dump(data_json, json_file)

