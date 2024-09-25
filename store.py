from typing import List, Tuple
import products


class Store:
    def __init__(self, products: List[products.Product] = None):
        if products is None:
            products = []
        self.products = products

    def add_product(self, product: products.Product):
        """
        Adds a product to the store
        :param product: Product
        """
        self.products.append(product)

    def remove_product(self, product: products.Product):
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

    def get_all_products(self) -> List[products.Product]:
        """
        Gets all products in the store
        :return: List[Product]
        """
        products = []
        for product in self.products:
            if product.is_active():
                products.append(product)

        return products

    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
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
