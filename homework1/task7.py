import numpy as np

def calculate_mean(numbers):
    num_mean = np.mean(numbers)
    return num_mean

def calculate_std_dev(numbers):
    std_deviatiation = np.std(numbers)
    return std_deviatiation


sample_data = [10, 20, 30, 40, 50]
print("Mean:", calculate_mean(sample_data))
print("Standard Deviation:", calculate_std_dev(sample_data))

def test_calculate_mean():
    data = [10, 20, 30, 40, 50]
    expected = sum(data) / len(data)  
    assert calculate_mean(data) == expected

def test_calculate_std_dev():
    data = [10, 20, 30, 40, 50]
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)  
    expected = variance ** 0.5  
    assert calculate_std_dev(data) == expected