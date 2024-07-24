import numpy as np


def compute_stationary_distribution(A, p):
    for _ in range(10000):
        p = p.dot(A)

    return p


def main():

    weather_matrix = np.array([[0.7, 0.2, 0.1], 
                               [0.2, 0.4, 0.4], 
                               [0.33, 0.33, 0.34]])

    initial_distribution = np.array([0.8, 0.1, 0.1])
    stationary_distribution = compute_stationary_distribution(weather_matrix, initial_distribution)
    print(f"Weather Matrix: {stationary_distribution}")

    Q1 = np.array([[0.1, 0.9, 0.0], 
                   [0.5, 0.0, 0.5], 
                   [0.7, 0.3, 0.0]])

    p0 = np.array([0.1, 0.6, 0.3])
    stationary_distribution = compute_stationary_distribution(Q1, p0)
    print(f"Problem Set Matrix: {stationary_distribution}")
    
if __name__ == "__main__":
    main()