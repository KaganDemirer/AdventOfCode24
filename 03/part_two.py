import re

def read_data(file="input.txt", mode="r"):
    with open(file, mode) as f:
        data = f.read()
    return data

def multiply(a,b):
    return a*b

def get_sorted_list_with_mul_do_dont(data):
    mults = []
    found_pattern = True
    while found_pattern:
        founds = []
        mul = re.search("mul\([0-9]+,[0-9]+\)", data)
        do = re.search("do\(\)", data)
        dont = re.search("don't\(\)", data)
        if mul:
            founds.append(mul)
        if do:
            founds.append(do)
        if dont:
            founds.append(dont)
        if len(founds) == 0:
            found_pattern = False
            break
        min_span_match = min(founds, key=lambda match: match.span()[0])
        mults.append(min_span_match.group())
        data = data[min_span_match.span()[1]:]
    return mults

data = read_data("03/input.txt")
mults = get_sorted_list_with_mul_do_dont(data)
res = 0
add = True
for x in mults:
    if x == "do()":
        add = True
        continue
    if x == "don't()":
        add = False
        continue
    one, two = x.split("(")[1].split(")")[0].split(",")
    if add: res += multiply(int(one), int(two))

print(res)