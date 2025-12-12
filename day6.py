import re

input = []

with open("day6input.txt", "r") as file:
    input = file.read().split("\n")[:-1]

for i in range(len(input)):
    input[i] = re.sub(r"\s+", " ", input[i])

input = [line.strip().split(" ") for line in input]
numbers = [[int(num) for num in row] for row in input[:-1]]
ops = input[-1]

total = 0

for i in range(len(ops)):
    use_mult = ops[i] == "*"
    start = 1 if use_mult else 0
    for row in numbers:
        if use_mult:
            start *= row[i]
        else:
            start += row[i]
    total += start

print(total)
