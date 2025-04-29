from abc import ABC, abstractmethod
from .products import Electronics, Accessories, Gadgets

class ProductsFactory(ABC):
    @abstractmethod
    def create_product(self, name, price, quantity, category=None):
        pass

class ElectronicsFactory(ProductsFactory):
    def create_product(self, **kwargs):
        return Electronics(
        name = kwargs.get('name'),
        price = kwargs.get('price'),
        quantity = kwargs.get('quantity'),
        category = kwargs.get('category'),
        warranty_period = kwargs.get('warranty_period')
        )
class AccessoriesFactory(ProductsFactory):
    def create_product(self, **kwargs):
        return Accessories(
        name = kwargs.get('name'),
        price = kwargs.get('price'),
        quantity = kwargs.get('quantity'),
        category = kwargs.get('category'),
        compatibility = kwargs.get('compatibility'))
class GadgetsFactory(ProductsFactory):
    def create_product(self, **kwargs):
        return Gadgets(
        name = kwargs.get('name'),
        price = kwargs.get('price'),
        quantity = kwargs.get('quantity'),
        category = kwargs.get('category'),
        features = kwargs.get('features')
        )

_FACTORY_MAP = {
    "electronics": ElectronicsFactory(),
    "accessories": AccessoriesFactory(),
    "gadgets": GadgetsFactory()
}

def get_product_factory(product_type) -> ProductsFactory:
    factory = _FACTORY_MAP.get(product_type.lower())
    if not factory:
        raise ValueError(f"Unknown product type: {product_type}")
    return factory