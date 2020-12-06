from math import ceil
f = open("aoc_5.txt", "r")

passes = []

for line in f:
    passes.append(line.strip("\n"))

seats = []

for seat in passes:
    row_start = 0
    col_start = 0
    row_end = 127
    col_end = 7
    for x in seat:
        if x == "F":
            row_end -= ceil((row_end - row_start) / 2)
        elif x == "B":
            row_start += ceil((row_end - row_start) / 2)
        elif x == "L":
            col_end -= ceil((col_end - col_start) / 2)
        elif x == "R":
            col_start += ceil((col_end - col_start) / 2)

    seats.append((row_end * 8) + col_end)

print (max(seats))
