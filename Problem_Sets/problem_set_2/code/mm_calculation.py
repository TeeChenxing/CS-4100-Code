import numpy as np


def compute_stationary_distribution(A, p, n_times):
    for _ in range(n_times):
        p = p.dot(A)
    return p


def main():
    weather_matrix = np.array([[0.7, 0.2, 0.1], 
                               [0.2, 0.4, 0.4], 
                               [0.33, 0.33, 0.34]])

    initial_distribution = np.array([0.8, 0.1, 0.1])
    stationary_distribution = compute_stationary_distribution(weather_matrix, initial_distribution, 10000)
    print(f"Weather Matrix Stationary Distribution: {stationary_distribution}")

    Q1 = np.array([[0.1, 0.9, 0.0], 
                   [0.5, 0.0, 0.5], 
                   [0.7, 0.3, 0.0]])

    p0 = np.array([0.1, 0.6, 0.3])
    stationary_distribution = compute_stationary_distribution(Q1, p0, 10000)
    print(f"Problem Set Matrix: {stationary_distribution}")

    q4_value = (0.409 * 0.5 * 0.9) + (0.409 * 0 * 0) + (0.409 * 0.5 * 0.3)
    print(f"Q4 Value: {q4_value}")

    q5_value = (0.1 * 0.1 * 0.9) + (0.1 * 0.9 * 0) + (0.1 * 0 * 0.3) + (0.6 * 0.5 * 0.9) + (0.6 * 0 * 0) + (0.6 * 0.5 * 0.3) + (0.3 * 0.7 * 0.9) + (0.3 * 0.3 * 0) + (0.3 * 0 * 0.3)
    print(f"Q5 Value: {q5_value}")

    #################################

    X_Y_S2 = compute_stationary_distribution(Q1, p0, 2)
    print(f"Q5 X --> Y --> 2: {X_Y_S2}")

    #################################

    coin_matrix = np.array([[0.5, 0.5], 
                            [0.34, 0.66]])

    initial_distribution = np.array([0.5, 0.5])
    stationary_distribution = compute_stationary_distribution(coin_matrix, initial_distribution, 10000)
    print(f"Coin Matrix Stationary Distribution: {stationary_distribution}")

if __name__ == "__main__":
    main()