from ..domain.order import Order
from ..domain.order_item import OrderItem
from ..domain.order_status import OrderStatus
from ..repository.order_repository import OrderRepository
from ..repository.product_catalog import ProductCatalog
from .exceptions import UnknownProductException
from .sell_items_request import OrderCreationCommand


class OrderCreationUseCase:
    def __init__(self, order_repository: OrderRepository, product_catalog: ProductCatalog):
        self._order_repository = order_repository
        self._product_catalog = product_catalog

    def run(self, cart: OrderCreationCommand) -> None:
        currency = 'EUR'
        order = Order(
            status=OrderStatus.CREATED,
            items=[],
            currency=currency,
            total=0,
            tax=0
        )

        for cart_item in cart.items:
            product = self._product_catalog.get_by_name(cart_item.product_name)

            if product is None:
                raise UnknownProductException()
            else:
                unitary_tax = round(product.price / 100 * product.category.tax_percentage, 2)
                unitary_taxed_amount = round((product.price + unitary_tax), 2)
                taxed_amount = round(unitary_taxed_amount * cart_item.quantity, 2)
                tax_amount = unitary_tax * cart_item.quantity

                order_item = OrderItem(
                    product=product,
                    quantity=cart_item.quantity,
                    tax=tax_amount,
                    taxed_amount=taxed_amount
                )
                order.items.append(order_item)

                order.total += taxed_amount
                order.tax += tax_amount

        self._order_repository.save(order)
