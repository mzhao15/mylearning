
import happybase

# create a happybase instance
connection = happybase.Connection('somehost')

"""to list available tables, use connection.tables()"""
print(connection.tables())

# working with tables

""" create a new table if it does not"""
""" cf1:col1     column family 1: column qualifier 1"""
connection.create_table(
    'mytable',
    {'cf1': dict(max_versions=10),
     'cf2': dict(max_versions=1, block_cache_enabled=False),
     'cf3': dict(),  # use defaults
    }
)

"""obtain a Table instance to work with, passing it the table name"""
table = connection.table('mytable')

# retriving data from tables

"""Table.row(), which retrieves a single row from the table, and returns it as a dictionary mappin"""
row = table.row(b'row-key')
print(row[b'cf1:col1'])   # prints the value of cf1:col1

"""The Table.rows() method works just like Table.row(), but takes multiple row keys and returns 
those as (key, data) tuples:"""

rows = table.rows([b'row-key-1', b'row-key-2'])
for key, data in rows:
    print(key, data)


"""making more fine-grained selections"""
row = table.row(b'row-key', columns=[b'cf1:col1', b'cf1:col2'])
print(row[b'cf1:col1'])
print(row[b'cf1:col2'])


"""using a timestamp"""
row = table.row(b'row-key', timestamp=123456789)

# scanning over rows in a table
"""scanning all rows, very timely expensive"""
for key, data in table.scan():
    print(key, data)

"""iterate over all rows between row aaa (included) and xyz (not included)"""
for key, data in table.scan(row_start=b'aaa', row_stop=b'xyz'):
    print(key, data)

"""An alternative is to use a key prefix. For example, to iterate over all rows starting with abc"""

for key, data in table.scan(row_prefix=b'abc'):
    print(key, data)

# storing data
"""To store a single cell of data in our table"""
table.put(b'row-key', {b'cf:col1': b'value1', b'cf:col2': b'value2'})

"""Use the timestamp argument if you want to provide timestamps explicitly"""
table.put(b'row-key', {b'cf:col1': b'value1'}, timestamp=123456789)

# deleting data
table.delete(b'row-key')
table.delete(b'row-key', columns=[b'cf1:col1', b'cf1:col2'])

# performing batch mutations

try:
    with table.batch(transaction=True) as b:
        b.put(b'row-key-1', {b'cf:col1': b'value1', b'cf:col2': b'value2'})
        b.put(b'row-key-2', {b'cf:col2': b'value2', b'cf:col3': b'value3'})
        b.put(b'row-key-3', {b'cf:col3': b'value3', b'cf:col4': b'value4'})
        b.delete(b'row-key-4')
        raise ValueError("Something went wrong!")
except ValueError:
    # error handling goes here; nothing is sent to HBase
    pass
# when no error occurred, the transaction succeeded
















