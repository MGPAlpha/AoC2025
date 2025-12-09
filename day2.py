input = []

with open("day2input.txt", "r") as file:
    input = file.read().split(",")

total = 0

for ran in input:
    index = ran.index("-")
    start = int(ran[:index])
    end = int(ran[index+1:])
    for i in range(start, end+1):
        num_str = str(i)
        if len(num_str) % 2 == 1: continue
        part1 = num_str[:len(num_str)//2]
        part2 = num_str[len(num_str)//2:]
        if part1 == part2:
            total += i
    
print(total)