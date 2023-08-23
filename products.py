class superProduct:
    def __init__(self, price, name):
        self.name = name
        self.price = self.set_price(price)

    def set_price(self, price):
        price = round(price, 2)

        return price

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


class Product(superProduct):
    def __init__(self, price, name):
        super().__init__(price, name)


class Kit(superProduct):
    def __init__(self, components, name):
        self.child_components = self.set_components(components)

        price_of_components = self.get_price_of_components()
        price = price_of_components + price_of_components * 0.1
        price = round(price, 2)
        super().__init__(price, name)

    def set_components(self, components):
        return components

    def get_components(self):
        return self.child_components

    def get_price_of_components(self):
        price_of_components = 0
        for component in self.child_components:
            price_of_components += component.get_price()
        return price_of_components
