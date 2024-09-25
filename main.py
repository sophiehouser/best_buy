import products
import store


def list_products(store_obj: store.Store):
    """List all active products in the store."""
    print("\nProducts in Store:")
    for product in store_obj.get_all_products():
        print(product.show())


def show_total_quantity(store_obj: store.Store):
    """Show the total quantity of all products in the store."""
    total_quantity = store_obj.get_total_quantity()
    print(f"\nTotal quantity in store: {total_quantity}")


def make_order(store_obj: store.Store):
    """Allow user to order products by selecting from the available products and specifying quantity."""
    shopping_list = []

    while True:
        print("\n------")
        print("Press Enter to finish your order.")
        print("Available Products:")
        active_products = store_obj.get_all_products()

        for i, product in enumerate(active_products, start=1):
            print(f"{i}. {product.show()}")

        print("------")
        product_choice = input("Which product # do you want? ")

        if product_choice == '':
            break

        try:
            product_index = int(product_choice) - 1
            if product_index < 0 or product_index >= len(active_products):
                print("Invalid product number, please choose again.")
                continue

            product = active_products[product_index]

            # Ask for quantity
            quantity_input = input(f"What amount do you want for {product.name}? ")

            try:
                quantity = int(quantity_input)
                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue
                if (type(product) is products.LimitedProduct
                        and quantity > product.get_maximum()):
                    print(f"You can only order {product.get_maximum()} per order")
                    continue
                elif quantity > product.get_quantity() and type(product) is not products.NonStockedProduct:
                    print("Not enough quantity available.")
                    continue

                shopping_list.append((product, quantity))
                print("Product added to list!")
            except ValueError:
                print("Invalid quantity, please enter a valid number.")
        except ValueError:
            print("Invalid input, please enter a valid product number.")

    if shopping_list:
        try:
            total_price = store_obj.order(shopping_list)
            print(f"\nTotal price of your order: ${total_price:.2f}")
        except ValueError as e:
            print(f"Error processing order: {e}")
    else:
        print("No products were ordered.")


def show_menu(store_obj: store.Store) -> object:
    """Display the main menu and prompt user for input."""
    while True:
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        # Get user input
        choice = input("Please choose a number: ")

        if choice == '1':
            list_products(store_obj)

        elif choice == '2':
            show_total_quantity(store_obj)

        elif choice == '3':
            make_order(store_obj)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid option, please choose between 1-4.")


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]
    best_buy = store.Store(product_list)

    show_menu(best_buy)


if __name__ == "__main__":
    main()
