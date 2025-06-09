# Exercise 1 
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
squared = []

# for v in df['value']:
#     squared.append(v ** 2)

# df['squared'] = squared

def sqaured(value):
    return value ** 2

dataframe = df["value"].apply(sqaured)
print(dataframe)


# Exercise 2:
# evens = []
# for n in range(100):
#     if n % 2 == 0:
#         evens.append(n)

evens_corrected = [x for x in range(100) if x % 2 == 0] 

# Exercise 3
# Take the array [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# Create a new array list[Tuple(int, int)] of every combination that sums to 1
# Do it once where (0.1, 0.9) is the same (0.9, 0.1) and again when they are different

array =  [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
solution = set()
for i in range(len(array)):
    for j in range(i, len(array)):
        value_i = array[i]
        value_j = array[j]
        if value_i + value_j == 1:
            solution.add(tuple((array[i], array[j])))

print(solution)