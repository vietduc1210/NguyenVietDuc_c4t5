sizes = [4, 10, 150, 120, 34, 60, 85]

print("Hello my name is Duc and these are my sheep sizes")
print(sizes)

biggest_size = max(sizes)
print("Now my biggest sheep has size",biggest_size,"let's shear it")
sizes[sizes.index(biggest_size)] = 8
print("After shearing, here is my flock")
print(sizes)
print("MONTH 1 :")
for j in range(7):
    sizes[j] = sizes[j] + 50
print("One month passed, now here is my flock")
print(sizes)
biggest_size = max(sizes)
print("Now my biggest sheep has size", biggest_size, "let's shear it")
sizes[sizes.index(biggest_size)] = 8
print("After shearing, here is my flock")
print(sizes)
print("MONTH 2 : ")
for j in range(7):
    sizes[j] = sizes[j] + 50
print("One month passed, now here is my flock")
print(sizes)
biggest_size = max(sizes)
print("Now my biggest sheep has size", biggest_size, "let's shear it")
sizes[sizes.index(biggest_size)] = 8
print("After shearing, here is my flock")
print(sizes)
print("MONTH 3 : ")
for j in range(7):
    sizes[j] = sizes[j] + 50
biggest_size = max(sizes)
sizes[sizes.index(biggest_size)] = 8
print("After shearing, here is my flock")
print(sizes)

print("My flock has size in total", sum(sizes))
print("I would get", sum(sizes),"* 2$ = ", sum(sizes)*2, "$")