# variables
n = 0
print('n =', n)

n = 'abc'
print('n =', n)

m, n = 0, 'abc'
n, m, z = 0.12, 'abc', False
print(m, n, z)

n = n + 1
n += 1
print(n)

n = 4
n = None
print("n = ", n)


# if statements
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2


m, n = 1, 2
if ((n > 2 and n != m) or (n == m)):
    n += 1

# loops
n = 5
while n < 5:
    print(n)
    n += 1

for i in range(5):
    print(i)

for i in range(2, 6):
    print(i)
