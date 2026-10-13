#This program tests and counts the tolerance of some 100 ohm resistors, resistors with tolerance above 5 are binned, and the program will stop when 0 is entered by user
count_1_percent = 0
count_5_percent = 0
count_reject = 0

while True:
    resistance = float(input("Enter measured resistance (enter 0 to stop): "))
    
    if resistance == 0:
        break
        
    if resistance >= 99.0 and resistance <= 101.0:
        count_1_percent += 1
    elif resistance >= 95.0 and resistance <= 105.0:
        count_5_percent += 1
    else:
        count_reject += 1

print("1% tolerance count:", count_1_percent)
print("5% tolerance count:", count_5_percent)
print("Reject count:", count_reject)
