import numpy as np
import itertools


def calculate_single_sequence(X, Y, state, Obsv, stationary_dist):
    temp_value = 0
    for i in range(len(X)):
        if i == 0:
            temp_value = stationary_dist[X[i]] * Obsv[X[i]][Y[i]]
        else:
            temp_value *= (state[X[i-1]][X[i]] * Obsv[X[i]][Y[i]])
    
    return temp_value

def main():
    weather_state = np.array([[0.5, 0.3, 0.2],
                              [0.4, 0.2, 0.4],
                              [0.0, 0.3, 0.7]])
    
    mood_observation = np.array([[0.9, 0.1],
                                 [0.6, 0.4],
                                 [0.2, 0.8]])
    
    stationary_dist = np.array([0.218, 0.273, 0.509])

    # Happy, Happy, Sad
    mood_pattern = [1, 1, 0]

    # Generate all permutations of weather sequences of length 3 (since mood_pattern is of length 3)
    weather_permutations = list(itertools.product([0, 1, 2], repeat=len(mood_pattern)))

    all_probabilities = []

    for weather_pattern in weather_permutations:
        value = calculate_single_sequence(weather_pattern, mood_pattern, weather_state, mood_observation, stationary_dist)
        all_probabilities.append(value)
    
    # Find the max index and corresponding weather sequence
    max_index = np.argmax(all_probabilities)
    highest_prob_weather_sequence = weather_permutations[max_index]

    print(f"Highest Probability Value: {all_probabilities[max_index]}")
    print(f"Weather Sequence with Highest Probability: {highest_prob_weather_sequence}")

if __name__ == "__main__":
    main()