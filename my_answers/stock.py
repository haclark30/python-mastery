import csv
from decimal import Decimal


class Stock:
    types = (str, int, float)

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount


class DStock(Stock):
    types = (str, int, Decimal)


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
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))


if __name__ == "__main__":
    portfolio = read_portfolio('Data/portfolio.csv')
    print_portfolio(portfolio)
