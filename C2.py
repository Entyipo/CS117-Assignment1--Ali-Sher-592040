#This program takes some resistors in paralell and figures out their equivalent resistances
def parallel_resistance(resistors):
    inverse_sum = 0
    for r in resistors:
        inverse_sum = inverse_sum + (1 / r)
    return inverse_sum

print(1 / parallel_resistance([10, 10]))
print(1 / parallel_resistance([100, 200, 300]))
