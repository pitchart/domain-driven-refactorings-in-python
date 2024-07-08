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
