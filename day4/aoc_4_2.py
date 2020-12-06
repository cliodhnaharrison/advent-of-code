import re

f = open("aoc_4.txt", "r")

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
    byr = re.search(r'\bbyr:(19[2-9][0-9]|200[0-2])\b', x)
    iyr = re.search(r'\biyr:(201[0-9]|2020)\b', x)
    eyr = re.search(r'\beyr:(202[0-9]|2030)\b', x)
    hgt_in = re.search(r'\bhgt:(1[5-8][0-9]|19[0-3])cm\b', x)
    hgt_cm = re.search(r'\bhgt:(59|6[0-9]|7[0-6])in\b', x)
    hcl = re.search(r'\bhcl:#([0-9]|[a-f]){6}\b', x)
    ecl = re.search(r'\becl:(amb|blu|brn|gry|grn|hzl|oth)\b', x)
    pid = re.search(r'\bpid:[0-9]{9}\b', x)

    if byr and iyr and eyr and (hgt_in or hgt_cm) and hcl and ecl and pid:
        valid += 1

print (valid)
