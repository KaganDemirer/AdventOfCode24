def get_difference(a,b):
    return abs(b - a)

def read_data(file="input.txt", mode="r"):
    with open(file, mode) as f:
        data = f.readlines()
    return data

def check_for_safety(list):
    increasing = True
    if list[0] > list[1]:
        increasing = False
    for i, num in enumerate(list):
        if i != len(list) - 1:
            if increasing and num > list[i+1]:
                return False
            elif not increasing and num < list[i+1]:
                return False
            diff = get_difference(num, list[i+1])
            if diff < 1 or diff > 3:
                return False
    return True

data = read_data("02/input.txt")
data = [list(map(int, x.removesuffix("\n").split(" "))) for x in data]
safes = 0
for x in data:
    if check_for_safety(x):
        safes += 1
print(safes)