
a = int(input("a ="))
b = int(input("b = "))
c = int(input("c = "))
a*x**2 + b*x + c = 0
delta = b*b - 4*a*c
if delta <0:
    print("The inquation has no solution")

elif delta == 0:
    x = (-b)/(2*a)
    print("x = ", x)

else:
    x1=(-b+delta**0.5)/(2*a)
    x2=(-b-delta**0.5)/(2*a)
    print("x1 = ", x1)
    print("x2 = ", x2)


