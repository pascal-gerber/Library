#pathlib and json are both needed for this code
import pathlib
import json


theFile = pathlib.Path("data.json")

#read the file
print(theFile.read_text())

#detects if the file exists or not
if not theFile.exists():
    theFile.write_text("{}")

#loads the json file as main file
data = json.loads(theFile.read_text())

#content that belongs into the Json
data["David"] = "GreyBlue9"

#writes into the json file
theFile.write_text(json.dumps(data))


#thank you david for being such a Fu..... i mean great guy
#IMPORTANT: DO NOT CALL YOUR FIRST TEST FILE "json.py"!!!!!!!!
