import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sin_taylor(x, terms=10):
    result = 0
    for n in range(terms):
        result += ((-1)**n * x**(2*n+1)) / factorial(2*n+1)
    return result

def cos_taylor(x, terms=10):
    result = 0
    for n in range(terms):
        result += ((-1)**n * x**(2*n)) / factorial(2*n)
    return result

# Test the functions
angle_degrees = 30
angle_radians = math.radians(angle_degrees)

print(f"Angle: {angle_degrees} degrees")
print(f"Sin(θ) using Taylor series: {sin_taylor(angle_radians):.6f}")
print(f"Sin(θ) using math.sin:      {math.sin(angle_radians):.6f}")
print(f"Cos(θ) using Taylor series: {cos_taylor(angle_radians):.6f}")
print(f"Cos(θ) using math.cos:      {math.cos(angle_radians):.6f}")