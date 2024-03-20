import numpy as np

# Define the objective function (e.g., Rosenbrock function)
def objective(x):
    return np.sum(100.0 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

def gradient(x):
    grad = np.zeros_like(x)
    grad[0] = -400 * x[0] * (x[1] - x[0]**2) - 2 * (1 - x[0])
    grad[1:-1] = 200 * (x[1:-1] - x[:-2]**2) - 400 * x[1:-1] * (x[2:] - x[1:-1]**2)
    grad[-1] = 200 * (x[-1] - x[-2]**2)
    return grad

# Define the gradient descent optimization algorithm
def gradient_descent(obj_fn, gradient_fn, initial_params, lr=0.01, num_steps=100):
    params = initial_params.copy()
    for i in range(num_steps):
        grad = gradient_fn(params)
        params -= lr * grad
        # Optionally, you can print the objective value at each step
        # print("Step {}: Objective = {}".format(i, obj_fn(params)))
    return params

# Initialize parameters and perform gradient descent optimization
initial_params = np.array([-1.5, 2.5])  # Initial guess
final_params = gradient_descent(objective, gradient, initial_params)

print("Optimal Parameters:", final_params)
print("Optimal Objective Value:", objective(final_params))
