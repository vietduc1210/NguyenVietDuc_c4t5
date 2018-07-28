from turtle import*
edge = 3
color("red")
for i in range(5):
    for j in range(edge):
        left(360/edge)
        forward(100)
    edge += 1
    if edge%6 == 0:
        color("yellow")
    elif edge%6 == 1:
        color("grey")
    elif edge%6 == 4:
        color("blue")
    elif edge%6 == 5:
        color("brown")


mainloop()

