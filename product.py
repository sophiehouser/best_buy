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


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
