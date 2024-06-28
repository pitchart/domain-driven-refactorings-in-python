from dataclasses import dataclass, field

from .sell_item_request import CartItem


@dataclass
class OrderCreationCommand:
    items: list[CartItem] = field(default_factory=list)
