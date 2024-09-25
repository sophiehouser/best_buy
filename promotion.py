from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        """applies half off promotion to the product"""
        discounted_items = quantity // 2
        full_price_items = quantity - discounted_items
        return (full_price_items * product.price) + (discounted_items * product.price * 0.5)


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        """applies third product free promotion"""
        return (quantity - quantity // 3) * product.price


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        """applies percent discount promotion to the product"""
        return quantity * product.price * (1 - self.percent / 100)