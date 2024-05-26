import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_simulations):
    results = {}
    count=0

    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        count+=1

        if total not in results:
            results[total] = 1
        else:
            results[total] += 1
        # print("count: ", count)
        # print("dice1: ", dice1)
        # print("dice2: ", dice2)
        # print("total: ", total)
        # print("results: ", results)
        # print("-"*60)

    probabilities = {key: value / num_simulations*100 for key, value in results.items()}
    return probabilities


# def plot_probabilities(probabilities):
#     x_values = list(probabilities.keys())
#     y_values = list(probabilities.values())

#     plt.bar(x_values, y_values, align="center", color='green')
#     plt.xlabel("Сума чиселдвох кубикаів")
#     plt.ylabel("Ймовірність, %")
#     plt.title("Ймовірності сум чисел на двох кубиках (Метод Монте-Карло)")
#     plt.show()

num_simulations=(12, 24, 36, 100, 1000, 10000)

if __name__ == "__main__":
    for i in num_simulations:
        num_simulations = i
        print("Запуск програми на кількість кидків кубика -", num_simulations)

        probabilities = simulate_dice_rolls(num_simulations)
        sorted_probabilities = dict(sorted(probabilities.items()))
        print("probabilities: ", probabilities)
        print("sorted_probabilities :", sorted_probabilities)

        print("Сума \t Ймовірність, %")
        for total, sorted_probabilities in sorted_probabilities.items():
            print(f"{total}\t {sorted_probabilities:.3f}")
        print("-"*100)
        print()
        
        #Побудова графіка розподілу ймовірностей метод Монте-Карло 
        x_values = list(probabilities.keys())
        y_values = list(probabilities.values())

        plt.bar(x_values, y_values, align="center", color='green')
        plt.xlabel("Сума чиселдвох кубикаів")
        plt.ylabel("Ймовірність, %")
        plt.title(f"Ймовірності сум чисел на двох кубиках (Монте-Карло) -{num_simulations} кидків")
        plt.show()