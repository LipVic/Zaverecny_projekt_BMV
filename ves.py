from PIL import Image
from random import randint
from funkcie import (
    filled_circle,
    circle,
    thick_line,
    fill_triangle,
    filled_rect,
    triangle,
    rectangle,
)


def render_ves(ves1):
    ves2 = ves1.splitlines()
    for i in ves2:
        if "VES" in i:
            prvky = i.split(" ")[2:4]
            width_a, height_a = int(float(prvky[0])), int(float(prvky[1]))
        if "CLEAR" in i:
            heks = i.split("#")[1]
            farba = tuple(int(heks[i : i + 2], 16) for i in (0, 2, 4))
            obr = Image.new("RGB", (width_a, height_a), farba)
        if "FILL_TRIANGLE" in i:
                hekss = i.split("#")[1]
                farba_tvaru = tuple(int(hekss[i : i + 2], 16) for i in (0, 2, 4))
                i = i.split(" ")
                A, B, C = tuple(i[1:3]), tuple(i[3:5]), tuple(i[5:7])
                A, B, C = (
                    tuple(int(float(w)) for w in A),
                    tuple(int(float(w)) for w in B),
                    tuple(int(float(w)) for w in C),
                )
                fill_triangle(obr, A, B, C, farba_tvaru)
                
        if "LINE" in i:
                hekss = i.split("#")[1]
                farba_tvaru = tuple(int(hekss[i : i + 2], 16) for i in (0, 2, 4))
                i = i.split(" ")
                A, B = tuple(i[1:3]), tuple(i[3:5])
                print(A)
                A, B = tuple(int(float(w)) for w in A), tuple(int(float(w)) for w in B)
                hrubka = int(float(i[5]))
                thick_line(obr, A, B, hrubka, farba_tvaru)
        if "FILL_CIRCLE" in i:
                hekss = i.split("#")[1]
                farba_tvaru = tuple(int(hekss[i : i + 2], 16) for i in (0, 2, 4))
                i = i.split(" ")
                S, r = tuple(i[1:3]), int(float(i[3]))
                S = tuple(int(float(w)) for w in S)
                filled_circle(obr, S, r, farba_tvaru)
        if "TRIANGLE" in i and "FILL" not in i:
                hekss = i.split("#")[1]
                farba_tvaru = tuple(int(hekss[i : i + 2], 16) for i in (0, 2, 4))
                i = i.split(" ")
                A, B, C = tuple(i[1:3]), tuple(i[3:5]), tuple(i[5:7])
                A, B, C = (
                    tuple(int(float(w)) for w in A),
                    tuple(int(float(w)) for w in B),
                    tuple(int(float(w)) for w in C),
                )
                hrubka = int(float(i[7]))
                triangle(obr, A, B, C, hrubka, farba_tvaru)
                
        if "FILL_RECT" in i:
                hekss = i.split("#")[1]
                farba_tvaru = tuple(int(hekss[i : i + 2], 16) for i in (0, 2, 4))
                i = i.split(" ")
                A, Width, Height = tuple(i[1:3]), int(float(i[3])), int(float(i[4]))
                A = tuple(int(float(w)) for w in A)
                filled_rect(obr, A, Width, Height, farba_tvaru)
                
        if "RECT" in i and "FILL" not in i:
                hekss = i.split("#")[1]
                farba_tvaru = tuple(int(hekss[i : i + 2], 16) for i in (0, 2, 4))
                i = i.split(" ")
                A, Width, Height, hrubka = (
                    tuple(i[1:3]),
                    int(float(i[3])),
                    int(float(i[4])),
                    int(float(i[5])),
                )
                A = tuple(int(float(w)) for w in A)
                rectangle(obr, A, Width, Height, hrubka, farba_tvaru)
        if "CIRCLE" in i and "FILL" not in i:
                hekss = i.split("#")[1]
                farba_tvaru = tuple(int(hekss[i : i + 2], 16) for i in (0, 2, 4))
                i = i.split(" ")
                S, r, hrubka = tuple(i[1:3]), int(float(i[3])), int(float(i[4]))
                S = tuple(int(float(w)) for w in S)
                circle(obr, S, r, hrubka, farba_tvaru)
    

    return obr
