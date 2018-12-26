import json

with open("test.json", "r+") as f:
    data = json.load(f)
    data["name"] = "xyz"
    data["age"] = "23"

    
    f.seek(0)
    json.dump(data, f, indent=2)
    f.truncate()
