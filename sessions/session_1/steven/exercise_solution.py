# Exercise 1 
import pandas as pd
from typing import List, Union

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
squared = []

for v in df['value']:
    squared.append(v ** 2)

df['squared'] = squared

# Exercise 1 solution:
def square_number(number: int) -> int:
    return number ** 2

df['squared_v2'] = df['value'].apply(square_number)

# Exercise 2:
evens = []
for n in range(100):
    if n % 2 == 0:
        evens.append(n)

def is_even(number: int) -> bool:
    return number % 2 == 0

# Exercise 2 solution
evens = [number for number in range(0, 100) if is_even(number)]

# Exercise 3
# Take the array [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# Create a new array list[Tuple(int, int)] of every combination that sums to 1
# Do it once where (0.1, 0.9) is the same (0.9, 0.1) and again when they are different
Number = Union[int, float]
number_array: List[Number] = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

def sums_to_1(num1: Number, num2: Number) -> bool:
    return num1 + num2 == 1

combinations = [[(num1, num2)] for num1 in number_array for num2 in number_array if sums_to_1(num1, num2)]

# A problem I had last week
# Create a function that will split a PDF by a title code
# For example titles of pattern ABC-123 (3 letters followed by 3 characters)
# Consider the logic when a title spans multiple pages 