#The program makes a function that takes 3 diffrent values and converts them into an equivalent value using the given formulas
def star_to_delta(ra, rb, rc):
    numerator = (ra * rb) + (rb * rc) + (rc * ra)
    rab = numerator / rc
    rbc = numerator / ra
    rca = numerator / rb
    return (rab, rbc, rca)

print(star_to_delta(10, 20, 30))
