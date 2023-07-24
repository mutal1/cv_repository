import numpy as np
import matplotlib.pyplot as plt

def create_function(x, a, b, c):
    return a * x**2 + b * x + c

def derivative_function(x, a, b):
    return 2 * a * x + b

# def newton_func(x, k, a, b, c):
#     return create_function(k, a, b, c) + derivative_function(k, a, b) * (x - k)

def newton_method(k, a, b, c, iterations=None):
    epsilon = 1e-15
    if iterations is None:
        iterations = []  

    new_k = k - (create_function(k, a, b, c) / derivative_function(k, a, b))
    iterations.append(new_k)  
    print("x", "=", new_k)
    print("func", "=", create_function(new_k, a, b, c))

    
    if abs(create_function(new_k, a, b, c)) <= epsilon:
        return new_k, iterations
    return newton_method(new_k, a, b, c, iterations)  

x = np.linspace(-100, 100, 20000)
y = create_function(x, 1, 0, -3)

root, iterations = newton_method(99, 8, 20, -61)


iterations = np.array(iterations)

plt.plot(x, y)
plt.scatter(iterations, create_function(iterations, 1, -4, 3), color='red', label='Root', zorder=5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Quadratic Function: f(x) = x^2 - 4x + 3')
plt.grid(True)
plt.axhline(y=0, color='black', linewidth=0.5)  # Add x-axis line
plt.axvline(x=0, color='black', linewidth=0.5)  # Add y-axis line
plt.legend()
plt.show()
