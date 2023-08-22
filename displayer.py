import os
from json_utils import convert_json_to_dict
class TreeDisplayer:
    def __init__(self):
        pass
    def display(self):
        json_path = self.ask_for_json()
        json_tree = convert_json_to_dict(json_path)
        print(json_tree)
        pass

    def ask_for_json(self):
        invalid_response = True
        while invalid_response:
            user_decision = input(f"What is the name of the json file you want to display? (e.g. productfamilyA.json)")
            json_path = f"json_files/{user_decision}"
            if os.path.exists(json_path):
                invalid_response = False
            else:
                print("Please write a file name that exists")
        return json_path
    