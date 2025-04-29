import config as cfg
from creational.factory.products_factory import get_product_factory

class ProductApp:
    def __init__(self):
        self.product_type = None

    def run(self):
        self.product_type = input("Enter product type (electronics/accessories/gadgets): ").strip().lower()
        factory = get_product_factory(self.product_type)
        
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        category = input("Enter product category: ")

        if self.product_type == "electronics":
            warranty_period = input("Enter warranty period: ")
            product = factory.create_product(name=name, price=price, quantity=quantity, category=category, warranty_period=warranty_period)
        elif self.product_type == "accessories":
            compatibility = input("Enter compatibility: ")
            product = factory.create_product(name=name, price=price, quantity=quantity, category=category, compatibility=compatibility)
        elif self.product_type == "gadgets":
            features = input("Enter features: ")
            product = factory.create_product(name=name, price=price, quantity=quantity, category=category, features=features)
        else:
            print(f"Unknown product type: {self.product_type}")
            return

        if product.save_to_db():
            print(f"{self.product_type.capitalize()} saved successfully!")
        else:
            print(f"Failed to save {self.product_type}.")

if __name__ == "__main__":
    app = ProductApp()
    app.run()