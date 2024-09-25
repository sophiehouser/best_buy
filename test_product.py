import pytest
from products import Product


def test_create_normal_product():
    product = Product("Test Product", 10.99, 100)
    assert product.name == "Test Product"
    assert product.price == 10.99
    assert product.quantity == 100
    assert product.is_active() is True


def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", 10.99, 100)  # Empty name

    with pytest.raises(ValueError):
        Product("Test Product", -5.99, 100)  # Negative price

    with pytest.raises(ValueError):
        Product("Test Product", 10.99, -10)  # Negative quantity


def test_product_becomes_inactive_at_zero_quantity():
    product = Product("Test Product", 10.99, 1)
    assert product.is_active() is True

    product.buy(1)
    assert product.quantity == 0
    assert product.is_active() is False


def test_product_purchase_modifies_quantity_and_returns_output():
    product = Product("Test Product", 10.99, 100)

    result = product.buy(5)
    assert product.quantity == 95
    assert result == 54.95  # 5 items at 10.99 each


def test_buying_larger_quantity_than_exists_raises_exception():
    product = Product("Test Product", 10.99, 10)

    with pytest.raises(ValueError):
        product.buy(15)
