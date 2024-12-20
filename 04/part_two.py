def read_data(file="input.txt", mode="r"):
    with open(file, mode) as f:
        data = [[char for char in x.removesuffix("\n")] for x in f.readlines()]
    return data

def get_XMAS(data, x, y):
    try:
        if x == 0 or y == 0:
            return False
        lt, lb, rt, rb = data[x-1][y+1], data[x-1][y-1], data[x+1][y+1], data [x+1][y-1]
        
        if ((lt == "M" and rb == "S") or (lt == "S" and rb == "M")) and ((lb == "M" and rt == "S") or (lb == "S" and rt == "M")):
            return True
    except:
        pass
    return False

data = read_data("04/input.txt")
counter = 0
for x, row in enumerate(data):
    for y, char in enumerate(row):
        if data[x][y] == "A":
            if get_XMAS(data, x, y):
                counter+=1

print(counter)