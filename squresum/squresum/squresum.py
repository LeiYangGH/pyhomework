#square = [
#    [2, 7, 6],
#    [9, 5, 1],
#    [4, 3, 8]
#]

square = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


def row_sums(square):
    re = square[0]
    n = len(re)
    for lst in square[1:]:
        sum = 0
        for i in range(n):
            re[i] = re[i] + lst[i]
    return re

print(row_sums(square))