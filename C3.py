#This program converts a positive decimal number to a binary string using repeated division by 2
def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary_result = ""
    while n > 0:
        remainder = n % 2
        binary_result = str(remainder) + binary_result
        n = n // 2
        
    return binary_result

print(decimal_to_binary(10))
print(decimal_to_binary(25))
