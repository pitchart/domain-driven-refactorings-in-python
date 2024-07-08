from abc import ABC, abstractmethod
from enum import Enum, auto

from typing_extensions import Self


class OrderStatus(Enum):
    APPROVED = auto()
    REJECTED = auto()
    SHIPPED = auto()
    CREATED = auto()


class OrderState(ABC):
    @abstractmethod
    def get_status(self) -> OrderStatus:
        pass

    @staticmethod
    def create(status: OrderStatus) -> Self:
        cases = {
            OrderStatus.CREATED: Created,
            OrderStatus.APPROVED: Approved,
            OrderStatus.REJECTED: Rejected,
            OrderStatus.SHIPPED: Shipped,
        }
        return cases.get(status)()


class Created(OrderState):

    def get_status(self) -> OrderStatus:
        return OrderStatus.CREATED


class Approved(OrderState):

    def get_status(self) -> OrderStatus:
        return OrderStatus.APPROVED


class Shipped(OrderState):

    def get_status(self) -> OrderStatus:
        return OrderStatus.SHIPPED


class Rejected(OrderState):

    def get_status(self) -> OrderStatus:
        return OrderStatus.REJECTED
