import stock


class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()


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
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


if __name__ == "__main__":
    portfolio = stock.read_portfolio('Data/portfolio.csv')
    formatter = create_formatter('text')
    print_table(portfolio, ['name', 'shares', 'price'], formatter)
    print_table(portfolio, ['shares', 'name'], formatter)
