def portfolio_cost(filename):
    sum = 0
    with open(filename, 'r') as f:
        for line in f:
            line_split = line.split()
            try:
                num_shares = int(line_split[1])
                price = float(line_split[2])
                sum += num_shares * price
            except ValueError as e:
                print(f"Couldn't parse {repr(line)}")
                print(f"Reason: {e}")
    return sum
if __name__ == "__main__":
    sum = portfolio_cost('/home/haclark/git/python-mastery/Data/portfolio3.dat')

    print(sum)