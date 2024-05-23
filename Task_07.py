import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_simulations):
    results = {}

    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2

        if total not in results:
            results[total] = 1
        else:
            results[total] += 1

    probabilities = {key: value / num_simulations for key, value in results.items()}
    return probabilities


def plot_probabilities(probabilities):
    x_values = list(probabilities.keys())
    y_values = list(probabilities.values())

    plt.bar(x_values, y_values, align="center", color='green')
    plt.xlabel("Сума чиселдвох кубикаів")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірності сум чисел на двох кубиках (Метод Монте-Карло)")
    plt.show()


if __name__ == "__main__":
    num_simulations = 100

    probabilities = simulate_dice_rolls(num_simulations)

    print("Сума \t Ймовірність")
    for total, probability in probabilities.items():
        print(f"{total}\t {probability:.3f}")

    plot_probabilities(probabilities)