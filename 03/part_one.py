import re

def read_data(file="input.txt", mode="r"):
    with open(file, mode) as f:
        data = f.read()
    return data

def multiply(a,b):
    return a*b

regEx = "mul\([0-9]+,[0-9]+\)"

data = read_data("03/input.txt")
mults = re.findall(regEx, data)
res = 0
for x in mults:
    one, two = x.split("(")[1].split(")")[0].split(",")
    res += multiply(int(one), int(two))

print(res)