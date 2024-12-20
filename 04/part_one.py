def read_data(file="input.txt", mode="r"):
    with open(file, mode) as f:
        data = [[char for char in x.removesuffix("\n")] for x in f.readlines()]
    return data

def get_XMAS(data, x, y, xx, yy):
    try:
        letters = ["X"]
        if (x <= 2 and xx == -1) or (y <= 2 and yy == -1):
            return False
        two, three, four = data[x+xx][y+yy], data[x+xx+xx][y+yy+yy], data[x+xx+xx+xx][y+yy+yy+yy]
        letters.append(two)
        letters.append(three)
        letters.append(four)
        if "XMAS" in "".join(letters):
            print(x,y,xx,yy)
            return True
    except:
        pass
    return False

data = read_data("04/input.txt")
counter = 0
for x, row in enumerate(data):
    for y, char in enumerate(row):
        if data[x][y] == "X":
            if get_XMAS(data, x, y, 1, 0):
                counter+=1
            if get_XMAS(data, x, y, -1, 0):
                counter+=1
            if get_XMAS(data, x, y, 0, 1):
                counter+=1
            if get_XMAS(data, x, y, 0, -1):
                counter+=1
            if get_XMAS(data, x, y, -1, -1):
                counter+=1
            if get_XMAS(data, x, y, 1, -1):
                counter+=1
            if get_XMAS(data, x, y, -1, 1):
                counter+=1
            if get_XMAS(data, x, y, 1, 1):
                counter+=1

print(counter)