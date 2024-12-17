f = open("day2.txt", "r")
score = 0
for line in f:
    line = line.strip("\n")

# Day 2 Part 1
    # if line == "A X":
    #   score += 4
    # elif line == "A Y":
    #   score += 8
    # elif line == "A Z":
    #   score += 3
    # elif line == "B X":
    #   score += 1
    # elif line == "B Y":
    #   score += 5
    # elif line == "B Z":
    #   score += 9
    # elif line == "C X":
    #   score += 7
    # elif line == "C Y":
    #   score += 2
    # elif line == "C Z":
    #   score += 6
    # else:
    #   print ("Error")

# Day 2 Part 2
    if line == "A X":
      score += 3
    elif line == "A Y":
      score += 4
    elif line == "A Z":
      score += 8
    elif line == "B X":
      score += 1
    elif line == "B Y":
      score += 5
    elif line == "B Z":
      score += 9
    elif line == "C X":
      score += 2
    elif line == "C Y":
      score += 6
    elif line == "C Z":
      score += 7
    else:
      print ("Error")
print (score)
