import json
import pathlib

#### some small extra, checking if the file exists
theFile = pathlib.Path("data.json")

#detects if the file exists or creates one
if not theFile.exists():
    theFile.write_text("{}")
##############################

#opens and loads the Json file named "data.json"
with open('data.json') as File:
    data = json.load(File)

#if empty doesn't print out
if len(data) != 0:
    #prints the value like a dictionnary value
    print(data['Name'])

#random name
import random
newRandomName = random.choice(["Jason", "Rebecca", "David", "Johnson", "Julia"])
#random name

#adds the random name under "new one"
data['Name'] = newRandomName

#dumps the data
with open('data.json', 'w') as File:
    json.dump(data, File, indent=2)
