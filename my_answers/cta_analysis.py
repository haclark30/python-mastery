from collections import Counter
from readrides import read_rides_as_dicts
from reader import read_csv_as_columns
from sys import intern


def num_routes(rides):
    routes = {r['route'] for r in rides}
    return len(routes)


def sum_day(rides, route, date):
    return sum([r['rides'] for r in rides if r['route'] == route and r['date'] == date])


def route_totals(rides):
    totals = Counter()
    for ride in rides:
        totals[ride['route']] += ride['rides']
    return totals


def ride_increase(rides, start_year, end_year):
    start_rides = [r for r in rides if r['date'].endswith(start_year)]
    end_rides = [r for r in rides if r['date'].endswith(end_year)]

    start_totals = route_totals(start_rides)
    end_totals = route_totals(end_rides)

    ride_inc = end_totals - start_totals
    return ride_inc


if __name__ == "__main__":
    rides = read_csv_as_columns('Data/ctabus.csv', [intern, intern, str, int])
    print(f"num routes: {num_routes(rides)}")
    print(f"day sum: {sum_day(rides, '22', '02/02/2011')}")
    print(route_totals(rides))
    print(f"increase: {ride_increase(rides, '2001', '2011').most_common(5)}")
