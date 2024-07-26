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
    print()

    ####################################################################

    which_coin_state = np.array([[0.5, 0.5], 
                                 [0.34, 0.66]])
    
    head_or_tails_observation = np.array([[0.5, 0.5],
                                          [0.7, 0.3]])
    
    coin_stationary_dist = np.array([0.4047619, 0.5952381])

    # Heads, Heads, Tails
    head_or_tails_pattern = [0, 0, 1]

    # Generate all permutations of coin type sequences of length 3 (since head_or_tails_pattern is of length 3)
    coin_type_permutations = list(itertools.product([0, 1], repeat=len(head_or_tails_pattern)))

    coin_all_probabilities = []

    print(f"Fair Coin is represented by 0 and Biased Coin is represented by 1.")
    for coin_type_pattern in coin_type_permutations:
        value = calculate_single_sequence(coin_type_pattern, head_or_tails_pattern, which_coin_state, head_or_tails_observation, coin_stationary_dist)
        coin_all_probabilities.append(value)
        
        print(f"Coin Type: {coin_type_pattern}, Probability: {value:.6f}")

    
    # Find the max index and corresponding coin sequence
    max_index = np.argmax(coin_all_probabilities)
    highest_prob_coin_type_sequence = coin_type_permutations[max_index]

    print(f"Highest Probability Value: {coin_all_probabilities[max_index]}")
    print(f"Coin Type Sequence with Highest Probability: {highest_prob_coin_type_sequence}")

if __name__ == "__main__":
    main()