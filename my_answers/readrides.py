# readrides.py
from collections import namedtuple
import csv

def trace_func(func, filename):
    import tracemalloc
    tracemalloc.start()
    rows = func(filename)
    print(f"Traced {func.__name__}")
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.stop()


def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dicts(filename):
    """Read ride data as list of dicts."""
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {'route': route, 'date': date, 'daytype': daytype, 'rides': rides}
            records.append(record)
    return records


def read_rides_as_class(filename):
    """Read ride data as a class"""
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_named_tuple(filename):

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = RowTuple(route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_slots(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = RowSlot(route, date, daytype, rides)
            records.append(record)
    return records


class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


class RowSlot:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

RowTuple = namedtuple('RowTuple', ['route', 'date', 'daytype', 'rides'])

if __name__ == '__main__':
    datafile = 'Data/ctabus.csv'
    trace_func(read_rides_as_tuples, datafile)
    trace_func(read_rides_as_dicts, datafile)
    trace_func(read_rides_as_class, datafile)
    trace_func(read_rides_as_named_tuple, datafile)
    trace_func(read_rides_as_slots, datafile)