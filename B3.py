# This program takes some sample values and checks which ones are above 3.2V, checks the highest voltage, lowest voltage and average voltage
readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)

count_above_3_2 = 0
highest = readings[0]
lowest = readings[0]
total_sum = 0
count = 0

for i in range(7):
    r = readings[i]
    
    if r > 3.2:
        count_above_3_2 = count_above_3_2 + 1
        
    if r > highest:
        highest = r
        
    if r < lowest:
        lowest = r
        
    total_sum = total_sum + r
    count = count + 1

average = total_sum / count

print("Readings above 3.2 V:", count_above_3_2)
print("Highest:", highest, "V")
print("Lowest:", lowest, "V")
print("Average:", average, "V")
