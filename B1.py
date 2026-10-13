#This program takes 10 voltage values from 1 to 10, and a fixed resistance value, 10 ohms. It then calculates the current for each of the 10 voltages

resistance=10

for voltage in range(1, 11):
    current=voltage/resistance
    print("Voltage=", voltage, "V", "Current=", current, "I")
    
    
