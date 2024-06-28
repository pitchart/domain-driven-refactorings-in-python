from dataclasses import dataclass

from typing_extensions import Self


@dataclass(frozen=True)
class Price:
    amount: float
    currency: str

    def add(self, price: Self) -> Self:
        # self._currencies_must_be_the_same(price)
        return Price(self.amount + price.amount, self.currency)

    def percent(self, percentage: float) -> Self:
        return Price(self.amount * percentage / 100, self.currency)

    def round(self):
        return Price(round(self.amount, 2), self.currency)

    def multiply(self, by):
        return Price(self.amount * by, self.currency)

    def __eq__(self, price: object) -> bool:
        if not isinstance(price, Price):
            return False
        return self.amount == price.amount and self.currency == price.currency
