#This program takes 3 resistor values, figures out the largest and smallest values, then displays them
R1 = int(input("Enter R1: "))
R2 = int(input("Enter R2: "))
R3 = int(input("Enter R3: "))

if R1 > R2:
    if R1 > R3:
        largest = R1
    else:
        largest = R3
else:
    if R2 > R3:
        largest = R2
    else:
        largest = R3

if R1 < R2:
    if R1 < R3:
        smallest = R1
    else:
        smallest = R3
else:
    if R2 < R3:
        smallest = R2
    else:
        smallest = R3

print("Smallest =", smallest, "ohm")
print("Largest =", largest, "ohm")
