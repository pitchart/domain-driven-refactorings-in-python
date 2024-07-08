from abc import ABC, abstractmethod
from enum import Enum, auto

from typing_extensions import Self

from src.domain.exceptions import ShippedOrdersCannotBeChangedException, RejectedOrderCannotBeApprovedException, \
    ApprovedOrderCannotBeRejectedException, OrderCannotBeShippedException, OrderCannotBeShippedTwiceException


class OrderStatus(Enum):
    APPROVED = auto()
    REJECTED = auto()
    SHIPPED = auto()
    CREATED = auto()


class OrderState(ABC):
    @abstractmethod
    def get_status(self) -> OrderStatus:
        pass

    @abstractmethod
    def approve(self) -> Self:
        pass

    @abstractmethod
    def reject(self) -> Self:
        pass

    @abstractmethod
    def ship(self) -> Self:
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

    def approve(self) -> OrderState:
        return Approved()

    def reject(self) -> OrderState:
        return Rejected()

    def ship(self) -> OrderState:
        raise OrderCannotBeShippedException()

    def get_status(self) -> OrderStatus:
        return OrderStatus.CREATED


class Approved(OrderState):

    def approve(self) -> OrderState:
        return self

    def reject(self) -> OrderState:
        raise ApprovedOrderCannotBeRejectedException()

    def ship(self) -> OrderState:
        return Shipped()

    def get_status(self) -> OrderStatus:
        return OrderStatus.APPROVED


class Shipped(OrderState):

    def approve(self) -> OrderState:
        raise ShippedOrdersCannotBeChangedException()

    def reject(self) -> OrderState:
        raise ShippedOrdersCannotBeChangedException()

    def ship(self) -> OrderState:
        raise OrderCannotBeShippedTwiceException()

    def get_status(self) -> OrderStatus:
        return OrderStatus.SHIPPED


class Rejected(OrderState):

    def approve(self) -> OrderState:
        raise RejectedOrderCannotBeApprovedException()

    def reject(self) -> OrderState:
        return self

    def ship(self) -> OrderState:
        raise OrderCannotBeShippedException()

    def get_status(self) -> OrderStatus:
        return OrderStatus.REJECTED
