import sys
print("enter the values of a, b and c in order to find the roots of given ax**2+bx+c equation.")
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])


def delta(a, b, c):
    f = b**2 - 4 * a * c
    return f


y = delta(a, b, c)


def solution1(a, b, c):
    g = (-b + (b**2 - 4 * a * c)**(1/2)) / (2 * a)
    return g


def solution2(a, b, c):
    h = (-b - (b**2 - 4 * a * c)**(1/2)) / (2 * a)
    return h


x1 = solution1(a, b, c)
x2 = solution2(a, b, c)

if y < 0:
    print("no real solution exists.")

elif y == 0:
    print("equation has repeated solutions.")
    print(f"both roots are {x1}")

elif y > 0:
    print("equation has two solutions.")
    print(f"the roots are {x1} and {x2}")
