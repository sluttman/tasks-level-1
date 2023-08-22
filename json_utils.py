import json

def insert_json_into_file(data, filename):
    with open(f"json_files/{filename}.json", "w") as json_file:
        json.dump(data, json_file, indent=2)  


