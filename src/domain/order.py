from .order_item import OrderItem
from .order_state import OrderState
from .order_status import OrderStatus
from .price import Price
from .product import Product


class Order:
    _id: int = 0
    _total: Price
    _currency: str = 'EUR'
    _items: list[OrderItem]
    _tax: Price
    _state: OrderState

    @property
    def id(self) -> int:
        return self._id

    @property
    def tax(self) -> Price:
        return self._tax

    @property
    def total(self) -> Price:
        return self._total

    @property
    def items(self) -> [OrderItem]:
        return self._items

    @property
    def currency(self) -> str:
        return self._currency

    @property
    def status(self) -> OrderStatus:
        return self._state.get_status()

    def __init__(self, id: int = 0, currency: str = 'EUR', status: OrderStatus = OrderStatus.CREATED) -> None:
        super().__init__()
        self._state = OrderState.create(status)
        self._tax = Price(0, currency)
        self._items = []
        self._currency = currency
        self._total = Price(0, currency)
        self._id = id

    def add_item_for(self, quantity: int, product: Product):
        order_item = OrderItem(product=product, quantity=quantity)
        self._items.append(order_item)
        self._total = self.total.add(order_item.taxed_amount)
        self._tax = self.tax.add(order_item.tax)

    def approve(self):
        self._state = self._state.approve()

    def reject(self):
        self._state = self._state.reject()

    def ship(self):
        self._state = self._state.ship()
