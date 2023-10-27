import csv
from decimal import Decimal


class Stock:
    __slots__ = ('name', '_shares', '_price')
    _types = (str, int, float)

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self._shares = shares
        self._price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def shares(self) -> int:
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f'Expected {self._types[1].__name__}')
        if value < 0:
            raise AttributeError('Shares must be non-negative')
        self._shares = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f'Expected {self._types[2].__name__}')
        if value < 0:
            raise AttributeError('Price must be non-negative')
        self._price = value

    @property
    def cost(self) -> float:
        return self._shares * self._price

    def sell(self, amount):
        self._shares -= amount

    def __repr__(self) -> str:
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Stock) and ((self.name, self.shares, self.price)
                                             == (other.name, other.shares, other.price))


class DStock(Stock):
    _types = (str, int, Decimal)


def read_portfolio(filename: str) -> "list[Stock]":
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = Stock.from_row(row)
            portfolio.append(record)

    return portfolio


def print_portfolio(portfolio: "list[Stock]"):
    print('%10s %10s %10s' % ("name", "shares", "price"))
    print(('-'*10 + ' ')*3)
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s._shares, s._price))


if __name__ == "__main__":
    portfolio = read_portfolio('Data/portfolio.csv')
    print_portfolio(portfolio)
