from string import ascii_uppercase


def generate_triangles(length=10, height=10, columns=6, rows=6):
    for row in range(0, rows):
        for column in range(0, columns):
            x, y, x1, y1 = (length * column, height * row, length * (column+1), height * (row+1))
            yield (ascii_uppercase[row] + str((column*2)+1), (x, y1), (x, y), (x1, y1))
            yield (ascii_uppercase[row] + str((column*2)+2), (x1, y), (x, y), (x1, y1))


def detect_triangle(v1, v2, v3, length=10, height=10, columns=6, rows=6):
    if any(x < 0 or x % length for x in (v1[0], v2[0], v3[0])) or \
       any(y < 0 or y % height for y in (v1[1], v2[1], v3[1])):
        raise ValueError("Invalid point")

    v2, v1, v3 = sorted([v1, v2, v3], key=lambda k: [k[1], k[0]])

    column, row = (v2[0] // length, v2[1] // height)

    if column >= columns or row >= rows:
        raise ValueError("Out of Bounds")

    if v2[0] < v1[0] and v2[0]+length == v1[0] and v2[0]+length == v3[0] and v2[1] == v1[1] and v2[1]+height == v3[1]:
        return ascii_uppercase[row] + str((column*2)+2)
    if v2[0] == v1[0] and v2[0]+length == v3[0] and v2[1]+height == v1[1] and v2[1]+height == v3[1]:
        return ascii_uppercase[row] + str((column*2)+1)

    raise ValueError("Invalid")
