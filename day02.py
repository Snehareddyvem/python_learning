a = 10
print(type(a))

b = 5.5
print(type(b))

c = 6+5j
print(type(c))

d = True
print(type(d))

e = None
print(type(e))


f = "sneha"
print(type(f))

g = [1,2,3,4,5]
print(type(g))

h = (1,2,3,4)
print(type(h))

i = {1,2,3,4}
print(type(i))

j = range(1,5,1)
print(type(j))

k = {"name": "xyz", "age":20}
print(type(k))

#type conversion-int to float
# int to float
a = 10
b = float(a)
print(type(b))

# float to int
c = 10.5
d = int(c)
print(type(d))

# int to string
e = 100
f = str(e)
print(type(f))

# string to int
g = "200"
h = int(g)
print(type(h))

# list to tuple
i = [1, 2, 3]
j = tuple(i)
print(type(j))

# tuple to list
k = (1, 2, 3)
l = list(k)
print(type(l))

# list to set
m = [1, 2, 2, 3]
n = set(m)
print(type(n))

# range to list
o = range(1, 6)
p = list(o)
print(type(p))