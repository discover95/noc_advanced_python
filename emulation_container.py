import re

class Field(dict):
    def adapt_key(self, item):
        column = str()
        line = int()
        if isinstance(item, (tuple, list)) and len(item) == 2:
            if re.match(r'^[a-zA-Z]$', str(item[0])):
                if re.match(r'^\d+$', str(item[1])) and int(item[1]) >= 0:
                    column = item[0]
                    line = int(item[1])
                else:
                    raise ValueError
            elif re.match(r'^[a-zA-Z]$', str(item[1])):
                if re.match(r'^\d+$', str(item[0])) and int(item[0]) >= 0:
                    column = item[1]
                    line = int(item[0])
                else:
                    raise ValueError
            else:
                raise ValueError
        elif isinstance(item, str):
            col_line = re.match(r'^(?P<column>[a-zA-Z])(?P<line>\d+)$', item)
            line_col = re.match(r'^(?P<line>\d+)(?P<column>[a-zA-Z])$', item)
            if col_line:
                column = col_line.group('column')
                line = int(col_line.group('line'))
            elif line_col:
                column = line_col.group('column')
                line = int(line_col.group('line'))
            else:
                raise ValueError
            if line < 0:
                raise ValueError
        else:
            raise TypeError
        return (column.lower(), line)

    def __getitem__(self, item):
        return super(Field, self).__getitem__(self.adapt_key(item))

    def __setitem__(self, key, value):
        return super(Field, self).__setitem__(self.adapt_key(key), value)

    def __delitem__(self, item):
        return super(Field, self).__delitem__(self.adapt_key(item))

    def __missing__(self, key):
        return None

    def __contains__(self, item):
        return self[item] != self.__missing__(1)

    def __iter__(self):
        return iter(super(Field, self).values())

# use
field = Field()

print(field['C5'] is None)

field[1, 'a'] = 25
field['a', 1] = 25
field['a', '1'] = 25
field['1', 'a'] = 25
field['1a'] = 25
field['a1'] = 25
field[1, 'A'] = 25
field['A', 1] = 25
field['A', '1'] = 25
field['1', 'A'] = 25
field['1A'] = 25
field['A1'] = 25

field[2, 'A'] = 50

print(field)

del field['2A']

for item in field:
    print(item)
