from .order_item import OrderItem
from .order_status import OrderStatus
from .price import Price


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
