from abc import ABC, abstractmethod
from enum import Enum, auto


class OrderStatus(Enum):
    APPROVED = auto()
    REJECTED = auto()
    SHIPPED = auto()
    CREATED = auto()


class OrderState(ABC):
    @abstractmethod
    def get_status(self) -> OrderStatus:
        pass


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
