from abc import ABC, abstractmethod
from datetime import datetime
import json
import config as cfg


class Products(ABC):
    def __init__(self, name, price, quantity, category=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.created_at = datetime.now()

    @abstractmethod
    def get_product_info(self):
        pass
    
    def store_product_info(self, data: dict) -> bool:
        if not isinstance(data, dict):
            return False
        
        with open(cfg.DB_DIR, 'r') as f:
            db = json.load(f)

        db.setdefault('products', []).append(data)

        with open(cfg.DB_DIR, 'w') as f:
            json.dump(db, f, indent=4, default=str) 
        return True
    
    def save_to_db(self):
        info = self.get_product_info()
        return self.store_product_info(info)
            

class Electronics(Products):
    def __init__(self, name, price, quantity, category, warranty_period):
        super().__init__(name, price, quantity, category)
        self.warranty_period = warranty_period

    def get_product_info(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category,
            "warranty_period": self.warranty_period,
            "created_at": self.created_at
        }


class Accessories(Products):
    def __init__(self, name, price, quantity, category, compatibility):
        super().__init__(name, price, quantity, category)
        self.compatibility = compatibility

    def get_product_info(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category,
            "compatibility": self.compatibility,
            "created_at": self.created_at
        }

class Gadgets(Products):
    def __init__(self, name, price, quantity, category, features):
        super().__init__(name, price, quantity, category)
        self.features = features

    def get_product_info(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category,
            "features": self.features,
            "created_at": self.created_at
        }