
class Validator:
    @classmethod
    def check(cls, value):
        return value


class Typed(Validator):
    expected_type = object

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)


class Integer(Typed):
    expected_type = int


class Float(Typed):
    expected_type = float


class String(Typed):
    expected_type = str


class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)


class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)


class PositiveInteger(Integer, Positive):
    pass


class PositiveFloat(Float, Positive):
    pass


class NonEmptyString(String, NonEmpty):
    pass


class Stock:
    __slots__ = ('name', '_shares', '_price')

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self) -> int:
        return self._shares

    @shares.setter
    def shares(self, value):
        self._shares = PositiveInteger.check(value)

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value):
        self._price = PositiveFloat.check(value)

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
