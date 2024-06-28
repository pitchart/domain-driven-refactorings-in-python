from dataclasses import dataclass, field

from .category import Category
from .price import Price


@dataclass
class Product:
    name: str = ""
    price: Price = Price(0, 'EUR')
    category: Category = field(default_factory=Category)
