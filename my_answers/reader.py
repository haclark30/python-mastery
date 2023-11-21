# import csv
# from collections import abc
# from abc import ABC, abstractmethod


# class CSVParser(ABC):
#     def parse(self, filename):
#         records = []
#         with open(filename) as f:
#             rows = csv.reader(f)
#             headers = next(rows)
#             for row in rows:
#                 record = self.make_record(headers, row)
#                 records.append(record)
#         return records

#     @abstractmethod
#     def make_record(self, headers, row):
#         pass


# class DictCSVParser(CSVParser):
#     def __init__(self, types) -> None:
#         self.types = types

#     def make_record(self, headers, row):
#         return {name: func(val) for name, func, val in zip(headers, self.types, row)}


# class InstanceCSVParser(CSVParser):
#     def __init__(self, cls) -> None:
#         self.cls = cls

#     def make_record(self, headers, row):
#         return self.cls.from_row(row)


# def read_csv_as_dicts(filename: str, coltypes: "list[function]"):
#     parser = DictCSVParser(coltypes)
#     return parser.parse(filename)


# class DataCollection(abc.Sequence):
#     def __init__(self, columns: "list[str]") -> None:
#         self.data = {col: [] for col in columns}

#     def __len__(self) -> int:
#         for k in self.data:
#             return len(self.data[k])

#     def __getitem__(self, index):
#         if isinstance(index, int):
#             return {col: self.data[col][index] for col in self.data}
#         elif isinstance(index, slice):
#             records = []
#             step = index.step if index.step is not None else 1
#             for i in range(index.start, index.stop, step):
#                 record = {col: self.data[col][i] for col in self.data}
#                 records.append(record)
#             return records

#     def append(self, data: "dict[str[any]]"):
#         for k, v in data.items():
#             self.data[k].append(v)


# def read_csv_as_columns(filename, typelist):
#     with open(filename) as f:
#         rows = csv.reader(f)
#         headings = next(rows)
#         records = DataCollection(headings)
#         for row in rows:
#             record = {name: func(val) for name, func,
#                       val in zip(headings, typelist, row)}
#             records.append(record)
#     return records


# def read_csv_as_instances(filename, cls):
#     '''Read CSV file into list of instances'''
#     parser = InstanceCSVParser(cls)
#     return parser.parse(filename)

# reader.py

import csv
from typing import Any, Dict, Iterable, List, Optional


def read_csv_as_dicts(filename: str, types: List[type]):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types)


def csv_as_dicts(lines: Iterable[str], types: List[type], headers: Optional[List[str]] = None) -> List[Dict[str, any]]:
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = {name: func(val)
                  for name, func, val in zip(headers, types, row)}
        records.append(record)
    return records


def read_csv_as_instances(filename: str, cls: type) -> List[Any]:
    '''
    Read CSV data into a list of instances
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls)


def csv_as_instances(lines: Iterable[str], cls: type, headers: Optional[List[str]] = None) -> List[Any]:
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(lines)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records
