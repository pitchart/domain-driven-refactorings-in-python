import pytest

from src.domain.price import Price


def ten_euros():
    return Price(10, 'EUR')


class TestPrice:

    def test_must_have_positive_value(self) -> None:
        with pytest.raises(ValueError, match='A price must be positive, -5.00 given'):
            Price(-5, 'EUR')

    def test_must_have_a_finite_value(self) -> None:
        with pytest.raises(ValueError, match='Price value must be finite'):
            Price(float('inf'), 'EUR')

    def test_can_add_to_another_price_when_currencies_are_the_same(self) -> None:
        five_euros = Price(5, 'EUR')

        sum = ten_euros().add(five_euros)

        assert sum == Price(15, 'EUR')

    def test_can_not_add_price_with_different_currencies(self) -> None:
        five_dollars = Price(5, 'USD')

        with pytest.raises(ValueError):
            ten_euros().add(five_dollars)

    def test_can_apply_percentage(self) -> None:
        tax = ten_euros().percent(10)

        assert tax == Price(1, 'EUR')

    def test_can_multipy_by_value(self) -> None:
        twice = ten_euros().multiply(by=2)

        assert twice == Price(20, 'EUR')

    def test_can_round_price(self) -> None:
        price = Price(10.256, 'EUR')

        rounded = price.round()

        assert rounded == Price(10.26, 'EUR')
