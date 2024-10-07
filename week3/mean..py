import numpy as np
from statistics import mode, StatisticsError

def calculate_statistics(numbers):
    """Calculate mean, median, and mode of a list of numbers."""
    
    mean_value = np.mean(numbers)
    median_value = np.median(numbers)


    try:
        mode_value = mode(numbers)
    except StatisticsError:
        mode_value = "No unique mode"

    return mean_value, median_value, mode_value


numbers = [1, 2, 2, 3, 4, 5, 5, 5, 6]
mean, median, mode_value = calculate_statistics(numbers)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode_value}")
