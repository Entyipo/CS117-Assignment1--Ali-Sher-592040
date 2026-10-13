#This program calculates loaded voltage, by calculating the equivalent resistance of the resistor attached to load resistor and then using the standard formula, but using equivalent resistance
def loaded_divider(vs, r1, r2, rl):
    v_unloaded = vs * (r2 / (r1 + r2))
    r_parallel = (r2 * rl) / (r2 + rl)
    v_loaded = vs * (r_parallel / (r1 + r_parallel))
    return (v_unloaded, v_loaded)

print(loaded_divider(12, 1000, 1000, 500))
