#This program checks the direction of current or whether it is flowing or not based off of it's value
current = float(input("Enter current value: "))

if current > 0:
    print("Current flows from A to B")
elif current < 0:
    print("Current flows from B to A")
else:
    print("No current flows")
