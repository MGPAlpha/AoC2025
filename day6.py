import re

input = []

with open("day6input.txt", "r") as file:
    input = file.read().split("\n")[:-1]

input = [row + " " for row in input]

numbers = input[:-1]
ops = input[-1]

total = 0

curr_op = None
running_op_val = None

for i in range(len(ops)):
    if curr_op == None:
        curr_op = ops[i]
        running_op_val = 1 if curr_op == "*" else 0
    curr_val = 0
    for j in range(len(numbers)):
        val = numbers[j][i]
        if val == " ":
            continue
        curr_val *= 10
        curr_val += int(val)
    if curr_val == 0: #Empty column == calculation done
        total += running_op_val
        print(running_op_val)
        curr_op = None
        running_op_val = 0
    else:
        print(curr_val)
        if curr_op == "+":
            running_op_val += curr_val
        else:
            running_op_val *= curr_val 



print(total)
