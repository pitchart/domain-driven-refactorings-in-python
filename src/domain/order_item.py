from .price import Price
from .product import Product


class OrderItem:
    product: Product
    quantity: int
    taxed_amount: Price
    tax: Price

    def __init__(self, product: Product, quantity: int) -> None:
        super().__init__()
        unitary_tax = product.price.percent(product.category.tax_percentage).round()
        self.tax = unitary_tax.multiply(by=quantity)
        self.taxed_amount = unitary_tax.add(product.price).round().multiply(by=quantity).round()
        self.quantity = quantity
        self.product = product
