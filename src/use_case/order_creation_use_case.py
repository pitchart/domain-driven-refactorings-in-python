from .exceptions import UnknownProductException
from .sell_items_request import OrderCreationCommand
from ..domain.order import Order
from ..domain.order_status import OrderStatus
from ..repository.order_repository import OrderRepository
from ..repository.product_catalog import ProductCatalog


class OrderCreationUseCase:
    def __init__(self, order_repository: OrderRepository, product_catalog: ProductCatalog):
        self._order_repository = order_repository
        self._product_catalog = product_catalog

    def run(self, cart: OrderCreationCommand) -> None:
        currency = 'EUR'
        order = Order(currency=currency, status=OrderStatus.CREATED)

        for cart_item in cart.items:
            product = self._product_catalog.get_by_name(cart_item.product_name)

            if product is None:
                raise UnknownProductException()

            order.add_item_for(quantity=cart_item.quantity, product=product)

        self._order_repository.save(order)
