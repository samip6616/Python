import math

def F(x):
    return math.log(x) + 2*x**2 + x - 3

def F_prime(x):
    return 1/x + 4*x + 1

# Initial guess
x_n = 1.0
tolerance = 1e-7
max_iterations = 1000
iterations = 0

while iterations < max_iterations:
    x_n1 = x_n - F(x_n) / F_prime(x_n)
    
    if abs(x_n1 - x_n) < tolerance:
        break

    x_n = x_n1
    iterations += 1

print(f"Root: {x_n}")