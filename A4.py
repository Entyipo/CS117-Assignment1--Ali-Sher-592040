#This program takes 2 bits and shows the result of their AND, OR and XOR gates
A = int(input("Enter A: "))
B = int(input("Enter B: "))

if A == 0:
    if B == 0:
        print("AND = 0")
        print("OR = 0")
        print("XOR = 0")
    elif B == 1:
        print("AND = 0")
        print("OR = 1")
        print("XOR = 1")
    else:
        print("Bits must be 0 or 1")
elif A == 1:
    if B == 0:
        print("AND = 0")
        print("OR = 1")
        print("XOR = 1")
    elif B == 1:
        print("AND = 1")
        print("OR = 1")
        print("XOR = 0")
    else:
        print("Bits must be 0 or 1")
else:
    print("Bits must be 0 or 1")
