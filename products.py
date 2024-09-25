class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid values for name, price, or quantity.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        """
        Get quality
        :return: float
        """
        return float(self.quantity)

    def set_quantity(self, quantity: int):
        """
        Set quantity
        :param quantity: int
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Check if product is active
        :return: bool
        """
        return self.active

    def activate(self):
        """
        Activate product
        """
        self.active = True

    def deactivate(self):
        """
        Deactivate product
        """
        self.active = False

    def show(self) -> str:
        """
        Show product
        :return:
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buy product
        :param quantity: int
        :return: float
        """
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock to fulfill the purchase.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)

        return total_price


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=1)

    def set_quantity(self, quantity: int):
        pass

    def buy(self, quantity: int) -> float:
        return self.price * quantity

    def show(self) -> str:
        return f"{self.name} - ${self.price:.2f} (Digital Product)"

class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def get_maximum(self) -> int:
        return self.maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(f"You can only purchase up to {self.maximum} of this product per order.")
        return super().buy(quantity)

    def show(self) -> str:
        return f"{self.name} - ${self.price:.2f} (Max {self.maximum} per order)"

