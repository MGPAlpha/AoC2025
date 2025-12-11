def test_in_searchable_range(searchable, val):
    if len(searchable) == 0: return (-1, False)
    lower_bound = 0
    upper_bound = len(searchable)
    while True:
        if lower_bound == upper_bound: # Failed to find value in ranges
            if lower_bound == len(searchable) or val < searchable[lower_bound][0]:
                return (lower_bound - 1, False)
            else:
                return (lower_bound, False)
        test_index = (upper_bound + lower_bound) // 2
        test_range = searchable[test_index]
        if val >= test_range[0] and val < test_range[1]: # value is within test range
            return (test_index, True)
        elif val < test_range[0]:
            upper_bound = test_index
        elif val >= test_range[1]:
            lower_bound = test_index + 1

def insert_new_range(searchable, new_range):
    start_index = test_in_searchable_range(searchable, new_range[0])
    if not start_index[1]: start_index = test_in_searchable_range(searchable, new_range[0]-1)
    end_index = test_in_searchable_range(searchable, new_range[1])
    if not end_index[1]: end_index = test_in_searchable_range(searchable, new_range[1]-1)

    extend_existing = start_index[1]
    range_end = new_range[1]
    if end_index[0] > -1:
        range_end = max(searchable[end_index[0]][1], range_end)
    num_deleted_ranges = end_index[0] - start_index[0]
    for _ in range(num_deleted_ranges):
        searchable.pop(start_index[0]+1)
    if extend_existing:
        existing = searchable[start_index[0]]
        new_range = (existing[0],range_end)
        searchable[start_index[0]] = new_range

    else: searchable.insert(start_index[0]+1, (new_range[0], range_end))


fresh_ranges = []
ids = []

with open("day5input.txt", "r") as file:
    input = file.read().strip().split("\n\n")
    fresh_ranges = input[0].split("\n")
    ids = input[1].split("\n")

searchable_range = []

for range_str in fresh_ranges:
    new_range = [int(n) for n in range_str.split("-")]
    new_range[1] += 1
    new_range = tuple(new_range)

    insert_new_range(searchable_range, new_range)

num_fresh = 0

for id in ids:
    id = int(id)
    search = test_in_searchable_range(searchable_range, id)
    if search[1]: num_fresh += 1

print(num_fresh)

total_possible_fresh = 0

for r in searchable_range:
    total_possible_fresh += r[1] - r[0]


print(total_possible_fresh)