# readrides.py
from collections import abc, namedtuple
from reader import read_csv_as_columns
from sys import intern
import csv


def trace_func(func, *args):
    import tracemalloc
    tracemalloc.start()
    rows = func(*args)
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
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {'route': route, 'date': date,
                      'daytype': daytype, 'rides': rides}
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


def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)


class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


class RideData(abc.Sequence):
    def __init__(self):
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self) -> int:
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, int):
            return {'route': self.routes[index],
                    'date': self.dates[index],
                    'daytype': self.daytypes[index],
                    'rides': self.numrides[index]}
        elif isinstance(index, slice):
            records = []
            step = index.step if index.step is not None else 1
            for i in range(index.start, index.stop, step):
                records.append({'route': self.routes[i],
                                'date': self.dates[i],
                                'daytype': self.dates[i],
                                'rides': self.numrides[i]})
            return records

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])


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
    trace_func(read_rides_as_columns, datafile)
    trace_func(read_csv_as_columns, datafile, [str, str, str, int])
    trace_func(read_csv_as_columns, datafile, [intern, intern, str, int])
