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
    old_dial = dial
    dial = dial + diff
    print("New Dial:", dial)
    if dial >= 100:
        score = score + dial // 100
    elif dial <= 0:
        score = score + (-dial // 100) + (1 if old_dial != 0 else 0) 
    dial = dial % 100
    print("Dial:", dial)
    print("Score:", score)
    
print("Final Score:", score)