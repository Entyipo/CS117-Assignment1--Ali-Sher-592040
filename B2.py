#This programs takes the number of resistors and calculates their sum
num_resistors = int(input("How many resistors? "))

total_resistance = 0

for i in range(1, num_resistors + 1):
    r_value = float(input("Enter R" + str(i) + ": "))
    total_resistance = total_resistance + r_value

print("Total resistance =", total_resistance, "ohm")
