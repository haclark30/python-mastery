import stock


def print_table(data, fields):
    print(' '.join('%10s' % f for f in fields))
    print(('-'*10 + ' ')*len(fields))

    for d in data:
        print(' '.join('%10s' % getattr(d, f) for f in fields))


if __name__ == "__main__":
    portfolio = stock.read_portfolio('Data/portfolio.csv')
    print_table(portfolio, ['name', 'shares', 'price'])
    print_table(portfolio, ['shares', 'name'])
