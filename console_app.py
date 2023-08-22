from products import *
from json_utils import insert_json_into_file
from displayer import *

class ConsoleApp:
    def __init__(self):
        self.dictionary_for_json_conversion = {}

    def run_app(self):
        print("Product App started!")
        user_decision = self.get_user_input()
        if user_decision == "add":
            self.create_product_tree()
        elif user_decision == "display":
            self.display_product_tree()
        

    def get_user_input(self):
        invalid_response = True
        while invalid_response:
            user_decision = input("Please tell me wether you want to to add a product tree manually or display the data! (add/display)")
            if user_decision.lower() in ["add", "display"]:
                invalid_response = False
            else:
                print("Please write either add or display")
        return user_decision
        

    def create_product_tree(self):
        print("creating product tree")
        creater = TreeCreater()
        tree = creater.create_manually()
        self.dictionary_for_json_conversion = self.create_dictionary(tree)
        filename = input("How would you like to call the file that the product tree will be stored in? \n (Beware that if the name already excists the old data will be overriden!)")
        insert_json_into_file(self.dictionary_for_json_conversion, filename)
        print(self.dictionary_for_json_conversion)
        pass

    def display_product_tree(self):
        print("displaying product tree")
        displayer = TreeDisplayer()
        displayer.display() 

    def create_dictionary(self, tree):
        dictionary = {}

        if type(tree) == Product:
            name_of_component = tree.get_name()
            price_of_component = tree.get_price()
            inserting_dict = {"name": name_of_component, "price": price_of_component, "type": "Product"}
            dictionary["product"] = inserting_dict
        elif type(tree) == Kit:
            name_of_component = tree.get_name()
            price_of_component = tree.get_price()
            inserting_dict = {"name": name_of_component, "price": price_of_component, "type": "Kit"}
            #dictionary["product_tree"] = inserting_dict
            components = tree.get_components()
            for i in range(0,len(components)):
                child_dictionary = self.create_dictionary(components[i])
                components_number = f"component_{str(i)}"
                inserting_dict[components_number] = child_dictionary
            dictionary.update(inserting_dict)
        
        return dictionary

class TreeCreater:
    def __init__(self):
        self.name_of_product = ""


    def create_manually(self):
        self.name_of_product = self.ask_for_name_of_product()
        number_of_child_products = self.ask_for_number_of_child_products()

        if number_of_child_products == 0:
            price_of_product = self.ask_for_price_of_product()  #float
            product = Product(price=price_of_product, name= self.name_of_product)
            return product
        
        else:
            list_of_components_of_kit =[]

            for number_child_product in range(0,number_of_child_products):
                print(f"Child Component Number {str(number_child_product + 1)} of {self.name_of_product}!")
                child_product = TreeCreater()                          # Here happens devide and conquer
                list_of_components_of_kit.append(child_product.create_manually())
            kit = Kit(components= list_of_components_of_kit, name=self.name_of_product)
            return kit

    def ask_for_name_of_product(self):
        user_decision = input("What is the Name of the Product/Kit you want to create?")
        
        return user_decision

    def ask_for_number_of_child_products(self):
        invalid_response = True
        while invalid_response:
            user_decision = input(f"How many components does your {self.name_of_product} consist of? (e.g. 0 or 3)")
            if self.is_whole_number(user_decision):
                invalid_response = False
            else:
                print("Please write only a number")
        return int(user_decision)
    
    def ask_for_price_of_product(self):
        invalid_response = True
        while invalid_response:
            user_decision = input(f"How much does {self.name_of_product} cost in €? (e.g. 100.33 or 32)")
            if self.is_number(user_decision):
                invalid_response = False
            else:
                print("Please write only a number")
        return float(user_decision)
    
    
    def is_whole_number(self, value):
        try:
            int_value = int(value)
            return isinstance(int_value, int)
        except ValueError:
            return False
        
    def is_number(self, value):
        try:
            int_value = float(value)
            return isinstance(int_value, float)
        except ValueError:
            return False

if __name__ == "__main__":
    app = ConsoleApp()
    app.run_app()


