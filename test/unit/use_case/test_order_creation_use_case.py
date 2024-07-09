import pytest

from src.domain.category import Category
from src.domain.exceptions import UnknownProductException
from src.domain.order_status import OrderStatus
from src.domain.price import Price
from src.domain.product import Product
from src.use_case.order_creation.order_creation_use_case import OrderCreationUseCase
from src.use_case.order_creation.sell_item_request import CartItem
from src.use_case.order_creation.sell_items_request import OrderCreationCommand
from test.doubles.in_memory_product_catalog import InMemoryProductCatalog
from test.doubles.test_order_repository import TestOrderRepository


class TestOrderCreationUseCase:
    def setup_method(self):
        self.order_repository = TestOrderRepository()
        self.product_catalog = InMemoryProductCatalog([
            Product(name='salad', price=Price(3.56, 'EUR'), category=Category(name='food', tax_percentage=10)),
            Product(name='tomato', price=Price(4.65, 'EUR'), category=Category(name='food', tax_percentage=10))
        ])
        self.use_case = OrderCreationUseCase(self.order_repository, self.product_catalog)

    def test_sell_multiple_items(self):
        request = OrderCreationCommand()
        request.items.append(CartItem(product_name='salad', quantity=2))
        request.items.append(CartItem(product_name='tomato', quantity=3))

        self.use_case.run(request)

        inserted_order = self.order_repository.inserted_order
        assert inserted_order.status == OrderStatus.CREATED
        assert inserted_order.total == Price(23.20, 'EUR')
        assert inserted_order.tax == Price(2.13, 'EUR')
        assert inserted_order.currency == 'EUR'
        assert len(inserted_order.items) == 2
        assert inserted_order.items[0].product.name == 'salad'
        assert inserted_order.items[0].product.price == Price(3.56, 'EUR')
        assert inserted_order.items[0].quantity == 2
        assert inserted_order.items[0].taxed_amount == Price(7.84, 'EUR')
        assert inserted_order.items[0].tax == Price(0.72, 'EUR')
        assert inserted_order.items[1].product.name == 'tomato'
        assert inserted_order.items[1].product.price == Price(4.65, 'EUR')
        assert inserted_order.items[1].quantity == 3
        assert inserted_order.items[1].taxed_amount == Price(15.36, 'EUR')
        assert inserted_order.items[1].tax == Price(1.41, 'EUR')

    def test_unknown_product(self):
        request = OrderCreationCommand()
        request.items.append(CartItem(product_name='unknown product', quantity=1))

        with pytest.raises(UnknownProductException):
            self.use_case.run(request)
