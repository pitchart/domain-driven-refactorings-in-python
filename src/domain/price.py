from dataclasses import dataclass

from typing_extensions import Self


@dataclass(frozen=True)
class Price:
    amount: float
    currency: str

    def __post_init__(self):
        self._value_must_be_positive()
        self._value_must_be_finite()
        pass

    def add(self, price: Self) -> Self:
        self._currencies_must_be_the_same(price)
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

    def _value_must_be_finite(self):
        if self.amount == float('inf'):
            raise ValueError('Price value must be finite')

    def _currencies_must_be_the_same(self, price: Self) -> None:
        if self.currency != price.currency:
            raise ValueError(f'Can not add prices in %s and %s'.format(self.currency, price.currency))

    def _value_must_be_positive(self) -> None:
        if self.amount < 0:
            raise ValueError(f"A price must be positive, {self.amount:.2f} given")
