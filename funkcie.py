def linePixels(A, B):
    pixels = []
    if A[0] == B[0]:
        if A[1] > B[1]:
            A, B = B, A
        for y in range(A[1], B[1] + 1):
            pixels.append((A[0], y))
    elif A[1] == B[1]:
        if A[0] > B[0]:
            A, B = B, A
        for x in range(A[0], B[0] + 1):
            pixels.append((x, A[1]))
    else:
        if A[0] > B[0]:
            A, B = B, A
        dx = B[0] - A[0]
        dy = B[1] - A[1]
        if abs(dy / dx) > 1:
            for y in range(min(A[1], B[1]), max(A[1], B[1]) + 1):
                x = int((y - A[1] + (dy / dx) * A[0]) * (dx / dy))
                pixels.append((x, y))
        else:
            for x in range(min(A[0], B[0]), max(A[0], B[0]) + 1):
                y = int((B[1] - A[1]) / (B[0] - A[0]) * (x - A[0]) + A[1])
                pixels.append((x, y))
    return pixels
def hranice(x, y, im):
    width, height = im.size
    return 0 <= x < width and 0 <= y < height


def line(im, A, B, color):
    if A[0] == B[0]:
        if A[1] > B[1]:
            A, B = B, A
        for y in range(A[1], B[1] + 1):
            if hranice(A[0], y, im):
                im.putpixel((A[0], y), color)
    elif A[1] == B[1]:
        if A[0] > B[0]:
            A, B = B, A
        for x in range(A[0], B[0] + 1):
            if hranice(x, A[1], im):
                im.putpixel((x, A[1]), color)
    else:
        if A[0] > B[0]:
            A, B = B, A
        dx = B[0] - A[0]
        dy = B[1] - A[1]
        if abs(dy / dx) > 1:
            for y in range(min(A[1], B[1]), max(A[1], B[1]) + 1):
                x = int((y - A[1] + (dy / dx) * A[0]) * (dx / dy))
                if hranice(x, y, im):
                    im.putpixel((x, y), color)
        else:
            for x in range(min(A[0], B[0]), max(A[0], B[0]) + 1):
                y = int((B[1] - A[1]) / (B[0] - A[0]) * (x - A[0]) + A[1])
                if hranice(x, y, im):
                    im.putpixel((x, y), color)
def filled_circle(im, S, r, color):
    for x in range(0, int(r / 2 ** (1 / 2)) + 1):
        y = int((r**2 - x**2) ** (1 / 2))
        line(im, (y + S[0], x + S[1]), (y + S[0], -x + S[1]), color)
        line(im, (x + S[0], y + S[1]), (x + S[0], -y + S[1]), color)
        line(im, (-x + S[0], y + S[1]), (-x + S[0], -y + S[1]), color)
        line(im, (-y + S[0], x + S[1]), (-y + S[0], -x + S[1]), color)
def circle(im, S, r, width, color):
    for x in range(0, int(r / 2 ** (1 / 2)) + 1):
        y = int((r**2 - x**2) ** (1 / 2))
        filled_circle(im, (x + S[0], y + S[1]), width, color)
        filled_circle(im, (y + S[0], x + S[1]), width, color)
        filled_circle(im, (y + S[0], -x + S[1]), width, color)
        filled_circle(im, (x + S[0], -y + S[1]), width, color)
        filled_circle(im, (-x + S[0], -y + S[1]), width, color)
        filled_circle(im, (-y + S[0], -x + S[1]), width, color)
        filled_circle(im, (-y + S[0], x + S[1]), width, color)
        filled_circle(im, (-x + S[0], y + S[1]), width, color)


def thick_line(im, A, B, thickness, color):
    pixels = linePixels(A, B)
    if thickness == 1:
        line(im, A, B, color)
    for X in pixels:
        filled_circle(im, X, thickness / 2, color)
def fill_triangle(im, A, B, C, color):
    V = sorted([A, B, C], key=getY)
    left = linePixels(V[0], V[1]) + linePixels(V[1], V[2])
    right = linePixels(V[0], V[2])

    Xmax = max(A[0], B[0], C[0])
    Xmin = min(A[0], B[0], C[0])

    if V[1][0] == Xmax:
        left, right = right, left

    for y in range(getY(V[0]), getY(V[2]) + 1):
        x1 = Xmax
        for X in left:
            if X[1] == y and X[0] < x1:
                x1 = X[0]

        x2 = Xmin
        for X in right:
            if X[1] == y and X[0] > x2:
                x2 = X[0]

        line(im, (x1, y), (x2, y), color)


def filled_rect(im, A, Width, Height, color):
    for x in range(A[0], A[0] + Width + 1):
        for y in range(A[1], A[1] + Height + 1):
            if hranice(x, y, im):
                im.putpixel((x, y), color)


def triangle(im, A, B, C, Thickness, color):
    if Thickness == 1:
        line(im, A, B, color)
        line(im, B, C, color)
        line(im, C, A, color)
    else:
        thick_line(im, A, B, Thickness, color)
        thick_line(im, B, C, Thickness, color)
        thick_line(im, C, A, Thickness, color)


def rectangle(im, A, width, height, thickness, color):
    thick_line(im, A, (A[0] + width, A[1]), thickness, color)
    thick_line(im, A, (A[0], A[1] + height), thickness, color)
    thick_line(
        im, (A[0], A[1] + height), (A[0] + width, A[1] + height), thickness, color
    )
    thick_line(
        im, (A[0] + width, A[1]), (A[0] + width, A[1] + height), thickness, color
    )
def getY(point):
    return point[1]