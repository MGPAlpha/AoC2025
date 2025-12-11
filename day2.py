input = []

def test_num(n):
    num_str = str(i)
    for seg_len in range(1,len(num_str)):
        if len(num_str) % seg_len != 0: continue
        part1 = num_str[:seg_len]
        len_works = True
        for seg_start in range(seg_len, len(num_str), seg_len):
            if part1 != num_str[seg_start: seg_start + seg_len]:
                len_works = False
                break
        if len_works: return True
    return False

with open("day2input.txt", "r") as file:
    input = file.read().split(",")

total = 0

for ran in input:
    index = ran.index("-")
    start = int(ran[:index])
    end = int(ran[index+1:])
    for i in range(start, end+1):
        if test_num(i):
            total += i
    
print(total)