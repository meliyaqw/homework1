# Homework

# Problem 1: solutions to HackerRank Python challenges

# 1
if __name__ == '__main__':
    print("Hello, World!")


# 2. 
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n % 2 == 1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")


# 3. 
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)


# 4. 
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)


# 5. 
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i ** 2)


# 6. 
def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False

    return leap

year = int(input())
print(is_leap(year))


# 7. 
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end='')


# 1. 
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i, j, k]
           for i in range(x + 1)
           for j in range(y + 1)
           for k in range(z + 1)
           if i + j + k != n])


# 2.
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = sorted(set(arr))
    print(scores[-2])


# 3. 
if __name__ == '__main__':
    students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

grades = sorted(set(score for name, score in students))

second_lowest = grades[1]

names = sorted(name for name, score in students if score == second_lowest)

for name in names:
    print(name)


# 4. 
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    average = sum(student_marks[query_name]) / 3
    print(f"{average:.2f}")


# 5. 
if __name__ == '__main__':
    N = int(input())
    arr = []

    for _ in range(N):
        command = input().split()

        if command[0] == 'insert':
            arr.insert(int(command[1]), int(command[2]))

        elif command[0] == 'print':
            print(arr)

        elif command[0] == 'remove':
            arr.remove(int(command[1]))

        elif command[0] == 'append':
            arr.append(int(command[1]))

        elif command[0] == 'sort':
            arr.sort()

        elif command[0] == 'pop':
            arr.pop()

        elif command[0] == 'reverse':
            arr.reverse()


# 6. 
if __name__ == '__main__':
    n = int(input())
    numbers = tuple(map(int, input().split()))

    mask = (1 << 64) - 1
    result = 0x345678
    multiplier = 1000003

    for i, number in enumerate(numbers):
        result = ((result ^ hash(number)) * multiplier) & mask
        multiplier += 82520 + 2 * (n - i - 1)

    result = (result + 97531) & mask

    if result >= (1 << 63):
        result -= (1 << 64)

    if result == -1:
        result = -2

    print(result)
# STRINGS

# 3
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# 4
def mutate_string(string, position, character):
    letters = list(string)
    letters[position] = character
    return ''.join(letters)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# 5
def count_substring(string, sub_string):
    count = 0

    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


# 6
if __name__ == '__main__':
    s = input()

print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))


# 7
thickness = int(input())
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))


# 8
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# 9
N, M = map(int, input().split())

for i in range(1, N, 2):
    print(('.|.' * i).center(M, '-'))

print('WELCOME'.center(M, '-'))

for i in range(N - 2, 0, -2):
    print(('.|.' * i).center(M, '-'))


# 10
def print_formatted(number):
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(decimal.rjust(width),
              octal.rjust(width),
              hexadecimal.rjust(width),
              binary.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# 11
def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lines = []

    for i in range(size):
        left = alphabet[size - 1:size - i - 1:-1]
        middle = alphabet[size - i - 1:size]
        line = '-'.join(left + middle)
        lines.append(line.center(4 * size - 3, '-'))

    print('\n'.join(lines + lines[-2::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# 12
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# 13
def minion_game(string):
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)


# 14
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        result = ''

        for char in substring:
            if char not in result:
                result += char

        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# Problem 2: algorythms 

# 1. Birthday Cake Candles
  #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

# 2. Number Line Jumps
  #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# 3. Viral Advertising
  #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# 4. Recursive Digit Sum
  #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

# 5. Insertion Sort - Part 1
  #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

# 6. Insertion Sort - Part 2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
