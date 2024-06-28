from dataclasses import dataclass


@dataclass
class CartItem:
    quantity: int = 0
    product_name: str = ""
