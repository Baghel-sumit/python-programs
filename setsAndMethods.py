a1 = {3, 4, 5, 5, 6, 7, 8, 8, 9, 9}
a2 = {3,4,5,6,7}
print(a1)
print('Type of a: ', type(a1))
print(a1.pop())
a1.add(33445)
print(a1)
print('Intersection', a1.intersection(a2))
print('union', a1.union(a2))
a3 = set()
print('Empty set', a3)
