# "+"演算子でリストを結合する
print([1, 2, 3] + [4, 5, 6])

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
c = a + b
print(c)

a.append(b)
print(a)

# a = a + b
a += b
print(a)