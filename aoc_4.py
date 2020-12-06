f = open("aoc_inputs/aoc_4.txt", "r")

passports = []
curr = ""

for line in f.readlines():
    if line != "\n":
        curr += line.strip("\n") + " "
    else:
        passports.append(curr)
        curr = ""
passports.append(curr)

valid = 0

for x in passports:
    if "byr:" in x and "iyr:" in x and "eyr:" in x and "hgt:" in x and "hcl:" in x \
    and "ecl:" in x and "pid:" in x:
        valid += 1

print (valid)
