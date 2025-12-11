input = []

def best_in_bank(bank, n):
    best_digit = -1
    best_index = -1
    for i in range(len(bank)-n+1):
        val = int(bank[i])
        if val > best_digit:
            best_digit = val
            best_index = i
    result = best_digit*pow(10,n-1)
    if (n>1):
        result += best_in_bank(bank[best_index+1:], n-1)
    return result

with open("day3input.txt", "r") as file:
    input = file.read().split("\n")[:-1]

total = 0

for bank in input:
    total += best_in_bank(bank, 2)

print(total)
