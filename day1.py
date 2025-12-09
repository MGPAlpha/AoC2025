input = []

with open("day1input.txt", "r") as file:
    input = file.read().split("\n")[:-1]

dial = 50
score = 0

for turn in input:
    print(turn)
    direction = 1 if turn[0] == "R" else -1
    diff = int(turn[1:])
    diff = diff * direction
    dial = (dial + diff) % 100
    if dial == 0:
        score = score + 1
    
print("Final Score:", score)