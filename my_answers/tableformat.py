import sys
import stock
from abc import ABC, abstractmethod


class TableFormatter(ABC):

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join('%s' % h for h in headers))

    def row(self, rowdata):
        print(','.join('%s' % d for d in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        header_tags = [f'<th>{h}</th>' for h in headers]
        header_tags.append('</tr>')
        header_tags.insert(0, '<tr>')
        print(' '.join(header_tags))

    def row(self, rowdata):
        data_tags = [f'<td>{d}</td>' for d in rowdata]
        data_tags.append('</tr>')
        data_tags.insert(0, '<tr>')
        print(' '.join(data_tags))


def create_formatter(type):
    if type == 'text':
        return TextTableFormatter()
    elif type == 'csv':
        return CSVTableFormatter()
    elif type == 'html':
        return HTMLTableFormatter()
    else:
        raise NotImplementedError("Unknown Formatter Type %s" % type)


def print_table(records, fields, formatter: TableFormatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


class redirect_stdout:
    def __init__(self, out_file) -> None:
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout


if __name__ == "__main__":
    portfolio = stock.read_portfolio('Data/portfolio.csv')
    formatter = create_formatter('text')
    print_table(portfolio, ['name', 'shares', 'price'], formatter)
    print_table(portfolio, ['shares', 'name'], formatter)

    with redirect_stdout(open('out.txt', 'w')) as f:
        print_table(portfolio, ['name', 'shares', 'price'], formatter)
        f.close()
