from .price import Price
from .product import Product


class OrderItem:
    _product: Product
    _quantity: int
    _taxed_amount: Price
    _tax: Price

    @property
    def product(self) -> Product:
        return self._product

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def tax(self) -> Price:
        return self._tax

    @property
    def taxed_amount(self) -> Price:
        return self._taxed_amount

    def __init__(self, product: Product, quantity: int) -> None:
        super().__init__()
        unitary_tax = product.price.percent(product.category.tax_percentage).round()
        self._tax = unitary_tax.multiply(by=quantity)
        self._taxed_amount = unitary_tax.add(product.price).round().multiply(by=quantity).round()
        self._quantity = quantity
        self._product = product
