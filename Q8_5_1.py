import numpy as np

target_error = 1.0e-5

def estimate_pi(num_points):
    x = np.random.uniform(0, 1, num_points)
    y = np.random.uniform(0, 1, num_points)
    
    distances = np.sqrt(x**2 + y**2)
    inside_circle = distances <= 1
    num_inside_circle = np.sum(inside_circle)
    
    pi_estimate = 4 * num_inside_circle / num_points
    return pi_estimate

def calculate_required_points(target_error):
    num_points = 0
    error = float('inf')
    
    while error > target_error:
        num_points += 1000  
        
        pi_estimate = estimate_pi(num_points)
        
        error = abs(pi_estimate - np.pi)
        
    return num_points, pi_estimate, error

required_points, pi_value, final_error = calculate_required_points(target_error)

print(f"必要な点の数: {required_points}")
print(f"推定されたπ: {pi_value}")
print(f"誤差: {final_error}")
