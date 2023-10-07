# tuples are immutable
t = (2, 3, 4, 5, 6)
print(t)
print('Type of tuple', type(t))
print('count', t.count(5))
print('indexing', t.index(3))
# t[1] = 'sumit' --> will through an error : 'tuple' object does not support item assignment
print('changing')
