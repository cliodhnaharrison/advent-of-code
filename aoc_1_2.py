f = open("aoc_inputs/aoc_1.txt", "r")
expenses = [int(x) for x in f.read().split('\n')[:-1]]

for i in range(len(expenses)):
    x = expenses[i]
    tmp = expenses[:i] + expenses[i+1:]
    for j in range(len(tmp)):
        y = tmp[j]
        tmp2 = tmp[:j] + tmp[j+1:]
        for k in range(len(tmp2)):
            if (x + y + tmp2[k]) == 2020:
                print (x * y * tmp2[k])
                break
