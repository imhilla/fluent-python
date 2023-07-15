# variables
from collections import deque
from multiprocessing import heap
import math

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

# loop in reverse order
for i in range(5, 1, -1):
    print(i)


# math
print(5/2)
print(5//2)
print(-3//2)
print(int(-3/2))

print(10 % 3)
print(-10 % 3)

# to be consistent with other math modulo

print(math.fmod(-10, 3))

print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(2))
print(math.pow(2, 3))

print(float("inf"))
print(float("-inf"))

print(math.pow(2, 200))
print(math.pow(2, 200) > float("inf"))

# Arrays
arr = [1, 2, 3]
print(arr)

arr.append(4)
arr.append(5)
print(arr)


arr.pop()
print(arr)

arr.insert(1, 7)
print(arr)

arr[0] = 0
print(arr)

n = 5
arr = [1] * n
print(arr)

arr = [1, 2, 3]
print(arr[-1])

arr = [1, 2, 3, 4]
print(arr[1:3])

print(arr[0:4])

a, b, c = [1, 2, 3]
print(a, b, c)

print(zip([1, 2, 3], [3, 4, 5]))

for n1, n2 in zip([1, 2, 3], [3, 4, 5]):
    print(n1, n2)


nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)

arr = [5, 7, 2, 8, 4, 70]
arr.sort()
print(arr)


arr.sort(reverse=True)
print(arr)

arr = ['bob', 'alice', 'jane', 'doe']
print(arr.sort())
print(arr)

arr.sort(key=lambda x: len(x))
print(arr)

# list comprehension
arr = [i for i in range(5)]
print(arr)

arr = [[0] * 4 for i in range(4)]
print(arr)

# strings
s = 'abc'
print(s[0:2])

# s[0] =  'A' error
# print(s)
s += 'def'
print(s)

strings = ["ab", "cd", "ef"]
print("".join(strings))


# queue
queue = deque()
queue.append(1)
queue.append(2)

print(queue)

queue.popleft()
print(queue)

queue.appendleft(3)
print(queue)

queue.pop()
print(queue)

# hashset

my_set = set()
my_set.add(1)
my_set.add(2)
print(my_set)
print(len(my_set))

print(1 in my_set)
print(2 in my_set)
print(3 in my_set)

my_set.remove(2)
print(my_set)

# list to set
print(set([1, 2, 2, 3]))

# set comprehension

my_set = {i for i in range(5)}
print(my_set)

# hash maps
my_map = {}
