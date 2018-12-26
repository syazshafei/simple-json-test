import json

with open("test2.json", "r+") as jsonFile:

    data = json.load(jsonFile)
    data["spec"]["dataSchema"]["parser"]["parseSpec"]["columns"] = "States","District","Cities","Latitude","Longitude","Sample_Population","Date","ISO","testtt"
    data["spec"]["dataSchema"]["parser"]["parseSpec"]["dimensionsSpec"]["dimensions"] = "States","Testtt","District","Cities",{"name": "Latitude","type": "float"}, {"name": "Longitude","type": "float"}, {"name": "Sample_Population","type": "long"}

    jsonFile.seek(0) #reset file position to the beginning
    json.dump(data, jsonFile, indent = 2)
    jsonFile.truncate() #remove remaining part



    #print(data["spec"]["dataSchema"]["parser"]["parseSpec"]["dimensionsSpec"]["dimensions"])
