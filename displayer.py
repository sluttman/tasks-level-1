import os
from json_utils import convert_json_to_dict
class TreeDisplayer:
    def __init__(self):
        pass
    def display(self):
        json_path = self.ask_for_json()
        json_tree = convert_json_to_dict(json_path)
        #component = self.ask_for_component()
        os.system("clear") #TODO use cls when using a Windows
        print(json_path + "\n")
        self.display_every_product_and_kit(json_tree, 0)
        #self.display_one_product_or_kit(json_tree)
        pass

    def ask_for_json(self):
        invalid_response = True
        while invalid_response:
            user_decision = input(f"What is the name of the json file you want to display components from? (e.g. productfamily.json write productfamily)\n")
            json_path = f"json_files/{user_decision}.json"
            if os.path.exists(json_path):
                invalid_response = False
            else:
                print("Please write a file name that exists")
        return json_path
    def display_every_product_and_kit(self, json_tree, indentation):
        
        self.display_one_product_or_kit(json_tree, indentation)
        for key in json_tree:
            if key not in ["name", "price", "type"]:

                self.display_every_product_and_kit(json_tree[key], indentation + 1)
        pass
    
    def display_one_product_or_kit(self, json_tree, indentation):
        indent = ""
        for i in range(0,indentation):
            indent = indent + "         "
        print(f"""{indent}{json_tree.get("name")}, Price: {json_tree.get("price")}, Type: {json_tree.get("type")}\n""")
        
