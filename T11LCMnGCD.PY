import math

def calculate_lcm_gcd(a, b):
    gcd = math.gcd(a, b)
    lcm = abs(a * b) // gcd
    return lcm, gcd


a = 12
b = 15
lcm, gcd = calculate_lcm_gcd(a, b)
print(f"LCM({a}, {b}) = {lcm}")
print(f"GCD({a}, {b}) = {gcd}")