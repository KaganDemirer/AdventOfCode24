def split_numbers(list):
    left_numbers = []
    right_numbers = []
    for x in list:
        ln, rn = x.split("   ")
        left_numbers.append(int(ln))
        right_numbers.append(int(rn.removesuffix("\n")))
    return left_numbers, right_numbers

def sort_list(list):
    return sorted(list)

def get_difference(a,b):
    return abs(b - a)

def read_data(file="input.txt", mode="r"):
    with open(file, mode) as f:
        data = f.readlines()
    return data

data = read_data("01/input.txt")
left_numbers, right_numbers = split_numbers(data)
left_numbers = sort_list(left_numbers)
right_numbers = sort_list(right_numbers)
result = 0
for i, num in enumerate(left_numbers):
    diff = get_difference(left_numbers[i], right_numbers[i])
    result += diff

print(result)