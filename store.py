from typing import List, Tuple
from product import *


class Store:
    def __init__(self, products: List[Product] = None):
        if products is None:
            products = []
        self.products = products

    def add_product(self, product: Product):
        """
        Adds a product to the store
        :param product: Product
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the store
        :param product:
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Calculates the total quantity of all products in the store
        :return: int
        """
        # Sum the quantities of all products in the store
        total_quantity = 0
        for product in self.products:
            if product.is_active():
                total_quantity += product.get_quantity()

        return total_quantity

    def get_all_products(self) -> List[Product]:
        """
        Gets all products in the store
        :return: List[Product]
        """
        products = []
        for product in self.products:
            if product.is_active():
                products.append(product)

        return products

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Creates an order
        :param shopping_list:
        :return: float
        """
        total_price = 0.0

        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"{product.name} is not available in the store.")

            total_price += product.buy(quantity)

        return total_price


if __name__ == '__main__':
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))
