def split_numbers(list):
    left_numbers = []
    right_numbers = []
    for x in list:
        ln, rn = x.split("   ")
        left_numbers.append(int(ln))
        right_numbers.append(int(rn.removesuffix("\n")))
    return left_numbers, right_numbers

def read_data(file="input.txt", mode="r"):
    with open(file, mode) as f:
        data = f.readlines()
    return data

def get_amount(num, right_numbers):
    return right_numbers.count(num)


data = read_data("01/input.txt")
left_numbers, right_numbers = split_numbers(data)
result = 0
for i, num in enumerate(left_numbers):
    amount = num * get_amount(num, right_numbers)
    result += amount

print(result)