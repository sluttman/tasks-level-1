from products import *

class ConsoleApp:
    def __init__(self):
        pass
    def run_app(self):
        print("Product App started!")
        user_decision = self.get_user_input()
        if user_decision == "add":
            self.create_product_tree()
        

    def get_user_input(self):
        invalid_response = True
        while invalid_response:
            user_decision = input("Please tell me wether you want to to add a product tree or display the data! (add/display)")
            if user_decision.lower() in ["add", "display"]:
                invalid_response = False
            else:
                print("Please write either add or display")
        return user_decision
        
    def create_product_tree(self):
        print("creating product tree")
        creater = TreeCreater()
        tree = creater.create()
        print(str(tree))
        pass

    def display_product_tree(self):
        print("displaying product tree")
        pass

class TreeCreater:
    def __init__(self):
        pass


    def create(self):
        name_of_product = self.ask_for_name_of_product()
        number_of_child_products = self.ask_for_number_of_child_products()

        if number_of_child_products == 0:
            price_of_product = self.ask_for_price_of_product()  #float
            product = Product(price=price_of_product, name= name_of_product)
            return product
        
        else:
            list_of_components_of_kit =[]

            for number_child_product in range(0,number_of_child_products):
                print(f"Child Component Number {str(number_child_product + 1)} of {name_of_product}!")
                child_product = TreeCreater()                          # Here happens devide and conquer
                list_of_components_of_kit.append(child_product.create())
            kit = Kit(components= list_of_components_of_kit, name=name_of_product)
            return kit

    def ask_for_name_of_product(self):
        user_decision = input("What is the Name of the Product/Kit you want to create?")
        
        return user_decision

    def ask_for_number_of_child_products(self):
        invalid_response = True
        while invalid_response:
            user_decision = input("How many components does your Product/Kit consist of? (e.g. 0 or 3)")
            if self.is_whole_number(user_decision):
                invalid_response = False
            else:
                print("Please write only a number")
        return int(user_decision)
    
    def ask_for_price_of_product(self):
        invalid_response = True
        while invalid_response:
            user_decision = input("How much does the product cost in €? (e.g. 100.33 or 32)")
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


