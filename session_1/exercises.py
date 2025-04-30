# Exercise 1 
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
squared = []

for v in df['value']:
    squared.append(v ** 2)

df['squared'] = squared
print(df)
# Exercise 2:
evens = []
for n in range(100):
    if n % 2 == 0:
        evens.append(n)

# Exercise 3
# Take the array [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# Create a new array list[Tuple(int, int)] of every combination that sums to 1
# Do it once where (0.1, 0.9) is the same (0.9, 0.1) and again when they are different

# A problem I had last week
# Create a function that will split a PDF by a title code
# For example titles of pattern ABC-123 (3 letters followed by 3 characters)
# Consider the logic when a title spans multiple pages 
