import string


def generate_triangles(length=10, height=10, columns=6, rows=6):
    for row in range(0, rows):
        for column in range(0, columns):
            x = length * column
            y = height * row
            yield (string.ascii_uppercase[row] + str((column*2)+1), (x, y+height), (x, y), (x+length, y+height))
            yield (string.ascii_uppercase[row] + str((column*2)+2), (x+length, y), (x, y), (x+length, y+height))


def detect_triangle(v1, v2, v3, length=10, height=10, columns=6, rows=6):
    if v2[0] % length or v2[1] % height or v1[0] % length or v1[1] % height or v3[0] % length or v3[1] % height:
        raise ValueError("Invalid point")

    column = v2[0] // length
    row = v2[1] // height

    if column >= columns or row >= rows:
        raise ValueError("Out of Bounds")

    if v2[0] < v1[0] and v2[0]+length == v1[0] and v2[0]+length == v3[0] and v2[1] == v1[1] and v2[1]+height == v3[1]:
        return string.ascii_uppercase[row] + str((column*2)+2)
    if v2[0] == v1[0] and v2[0]+length == v3[0] and v2[1]+height == v1[1] and v2[1]+height == v3[1]:
        return string.ascii_uppercase[row] + str((column*2)+1)

    raise ValueError("Invalid Order")