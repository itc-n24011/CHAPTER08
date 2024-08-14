import math
import random

target_error = 1.0e-5

def estimate_pi(num_points):
    inside_circle = 0
    
    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        
        if x**2 + y**2 <= 1:
            inside_circle += 1
    
    pi_estimate = 4 * inside_circle / num_points
    return pi_estimate

def calculate_required_points(target_error):
    num_points = 0
    error = float('inf')
    
    while error > target_error:
        num_points += 1000  
        
        pi_estimate = estimate_pi(num_points)
        
        error = abs(pi_estimate - math.pi)
        
    return num_points, pi_estimate, error

required_points, pi_value, final_error = calculate_required_points(target_error)

print(f"必要な点の数: {required_points}")
print(f"推定されたπ: {pi_value}")
print(f"誤差: {final_error}")

