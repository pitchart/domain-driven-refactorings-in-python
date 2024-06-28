from .price import Price
from .product import Product


class OrderItem:
    product: Product
    quantity: int
    taxed_amount: Price
    tax: Price

    def __init__(self, product: Product, quantity: int, taxed_amount: Price, tax: Price) -> None:
        super().__init__()
        self.tax = tax
        self.taxed_amount = taxed_amount
        self.quantity = quantity
        self.product = product
