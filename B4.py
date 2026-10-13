#This program takes some sample values and figures out the longest streak where samples decrease in value, it prints the longest lenght and the starting and ending voltages of the streak
voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

max_streak = 1
final_start = voltages[0]
final_end = voltages[0]

streak_count = 1
streak_start = voltages[0]

for i in range(len(voltages) - 1):
    current_reading = voltages[i]
    next_reading = voltages[i + 1]
    
    if next_reading < current_reading:
        if streak_count == 1:
            streak_start = current_reading
        streak_count = streak_count + 1
        streak_end = next_reading
    else:
        streak_count = 1
        
    if streak_count > max_streak:
        max_streak = streak_count
        final_start = streak_start
        final_end = streak_end

print("Longest continuous drop:", max_streak, "minutes")
print("Started at:", final_start, "V")
print("Ended at:", final_end, "V")
