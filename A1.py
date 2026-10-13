#This program uses Ohm's Law to calculate the current of a circuit, and whether it will blow or not
Voltage=float(input(" Enter Voltage (V): "))
Resistance=float(input("Enter Resistance (ohm): "))

if Resistance<=0:
    print("Invalid resistance")
else:
    print("Current: ", Voltage/Resistance, "A" )

if Voltage/Resistance >2:
    print("Fuse will blow")
else:
    print("Circuit is safe")

