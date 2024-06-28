from src.domain.price import Price


def ten_euros():
    return Price(10, 'EUR')


class TestPrice:

    def test_can_add_to_another_price_when_currencies_are_the_same(self) -> None:
        five_euros = Price(5, 'EUR')

        sum = ten_euros().add(five_euros)

        assert sum == Price(15, 'EUR')

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
