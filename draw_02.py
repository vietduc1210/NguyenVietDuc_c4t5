from turtle import*
angle = 3
color("red")

for i in range(4):
      for a in range(angle):

        left(360/angle)

        forward(100)

        angle += 1

        if pencolor() == "red":

            color("blue")

        else:

            color("red")



mainloop()

