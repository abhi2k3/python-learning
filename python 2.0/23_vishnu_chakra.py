list1 = [
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14],
    [15,16,17,18,19,20,21],
    [22,23,24,25,26,27,28],
    [29,30,31,32,33,34,35],
    [36,37,38,39,40,41,42],
    [43,44,45,46,47,48,49]
]
list2 = []
rows = 0
col = 0
max_row = 6
min_row = 0
max_col = 6
min_col = 0
while min_row <= max_row and min_col <= max_col:
    for col in range(min_col, max_col + 1):
        list2.append(list1[min_row][col])
    min_row += 1
    for rows in range(min_row, max_row + 1):
        list2.append(list1[rows][max_col])
    max_col -= 1
    if min_row <= max_row:
        for col in range(max_col, min_col - 1, -1):
            list2.append(list1[max_row][col])
        max_row -= 1
    if min_col <= max_col:
        for rows in range(max_row, min_row - 1, -1):
            list2.append(list1[rows][min_col])
        min_col += 1
print(list2)
