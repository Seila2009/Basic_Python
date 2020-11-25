from sys import argv


def zp_pers(a, b, c):
    return (a * b) + c


file_part, a, b, c = argv

print(zp_pers(int(a), int(b), int(c)))
