# List is mutable
l1 = [2, 3, 4, 5, 6, 6, "Sumit baghel"]
print(type(l1))
print(l1)
removingElement = 'Sumit baghel'
l1.remove(removingElement)
print('count of 1 digits : ', l1.count(1))
l1.pop()
print('list after mutation ', l1)
appendingElement = 2
l1.append(appendingElement)
l1.extend([89, 9384, 384])
print('indexing', l1.index(3))
print('After appending an element ', l1)
