import csv
from collections import abc


def read_csv_as_dicts(filename: str, coltypes: "list[function]"):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {name: func(val) for name, func,
                      val in zip(headers, coltypes, row)}
            records.append(record)
    return records


class DataCollection(abc.Sequence):
    def __init__(self, columns: "list[str]") -> None:
        self.data = {col: [] for col in columns}

    def __len__(self) -> int:
        for k in self.data:
            return len(self.data[k])

    def __getitem__(self, index):
        if isinstance(index, int):
            return {col: self.data[col][index] for col in self.data}
        elif isinstance(index, slice):
            records = []
            step = index.step if index.step is not None else 1
            for i in range(index.start, index.stop, step):
                record = {col: self.data[col][i] for col in self.data}
                records.append(record)
            return records

    def append(self, data: "dict[str[any]]"):
        for k, v in data.items():
            self.data[k].append(v)


def read_csv_as_columns(filename, typelist):
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        records = DataCollection(headings)
        for row in rows:
            record = {name: func(val) for name, func,
                      val in zip(headings, typelist, row)}
            records.append(record)
    return records


def read_csv_as_instances(filename, cls):
    '''Read CSV file into list of instances'''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
