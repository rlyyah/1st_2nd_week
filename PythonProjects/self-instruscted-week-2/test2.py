x = 10
y = x

print(id(x) == id(y))
print(id(y) == id(10))
print(id(x))
x = x + 1
print(id(x))
print(id(x) != id(y))
print(id(x) != id(10))

print('================')

m = list([1,2,3])
n = m
print(m)
print(n)

print(id(m) == id(n))

n.pop()
print(m)
print(n)
print(f"after poop: {id(m) == id(n)}")