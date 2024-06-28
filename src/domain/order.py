from .order_item import OrderItem
from .order_status import OrderStatus
from .price import Price
from .product import Product


class Order:
    id: int = 0
    total: Price
    currency: str = 'EUR'
    items: list[OrderItem]
    tax: Price
    status: OrderStatus

    def __init__(self, id: int = 0, currency: str = 'EUR', status: OrderStatus = OrderStatus.CREATED) -> None:
        super().__init__()
        self.status = status
        self.tax = Price(0, currency)
        self.items = []
        self.currency = currency
        self.total = Price(0, currency)
        self.id = id

    def add_item_for(self, quantity: int, product: Product):
        order_item = OrderItem(product=product, quantity=quantity)
        self.items.append(order_item)
        self.total = self.total.add(order_item.taxed_amount)
        self.tax = self.tax.add(order_item.tax)
