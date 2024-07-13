import random

def generate_and_print_random_biases():
    """
    Generate random biases 'a' and 'b' within the range [0, 1] and print them.

    Returns:
    - a: Random bias for the first coin.
    - b: Random bias for the second coin.
    """
    a = random.random()
    b = random.random()

    print("Random bias 'a':", a)
    print("Random bias 'b':", b)
    print()

    return a, b

def update_probabilities(prob_head, prob_tail, bias_a, bias_b):
    """
    Update probabilities of getting heads and tails based on biases 'a' and 'b'.

    Args:
    - prob_head: Probability of getting heads initially.
    - prob_tail: Probability of getting tails initially.
    - bias_a: Bias factor for the first coin.
    - bias_b: Bias factor for the second coin.

    Returns:
    - Updated probabilities of getting heads and tails.
    """
    new_prob_head = prob_head * bias_a + prob_tail * bias_b
    new_prob_tail = prob_head * (1 - bias_a) + prob_tail * (1 - bias_b)
    return new_prob_head, new_prob_tail

def main():
    # Define the number of coin tosses for different iterations
    iterations = [10, 100, 1000, 10000]

    # Define initial probabilities
    initial_probabilities = [[0.5, 0.5], [0, 1]]

    for initial_probability_pair in initial_probabilities:
        print("Initial probability of head:", initial_probability_pair[0])
        print("Initial probability of tail:", initial_probability_pair[1])
        print()

        for iteration in iterations:
            print("Number of iterations:", iteration)

            # Get initial probabilities
            prob_head, prob_tail = initial_probability_pair

            # Generate random biases
            a, b = generate_and_print_random_biases()

            for _ in range(iteration):
                # Update probabilities based on the randomly generated biases
                prob_head, prob_tail = update_probabilities(prob_head, prob_tail, a, b)

            # Print the final probabilities
            print("Probability of getting head after", iteration, "coin tosses:", prob_head)
            print("Probability of getting tail after", iteration, "coin tosses:", prob_tail)
            print()
        print()

if __name__ == "__main__":
    main()
