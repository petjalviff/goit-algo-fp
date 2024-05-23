items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    for item in items:
        items[item]['ratio'] = items[item]['calories'] / items[item]['cost']
    
    sorted_items = sorted(items.items(), key=lambda x: x[1]['ratio'], reverse=True)
    
    total_calories = 0
    chosen_items = []
    for item, values in sorted_items:
        if budget - values['cost'] >= 0:
            budget -= values['cost']
            total_calories += values['calories']
            chosen_items.append(item)
        else:
            continue
    
    return chosen_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.keys())
    cost = [items[item]['cost'] for item in item_list]
    calories = [items[item]['calories'] for item in item_list]
    
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if cost[i-1] <= w:
                dp[i][w] = max(calories[i-1] + dp[i-1][w-cost[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen_items.append(item_list[i-1])
            w -= cost[i-1]
    
    return chosen_items[::-1], dp[n][budget]

budget = 120 
greedy_items, greedy_calories = greedy_algorithm(items, budget)
dp_items, dp_calories = dynamic_programming(items, budget)

print("Жадібний алгоритм:")
print("Обрані страви:", greedy_items)
print("Загальна кількість калорій:", greedy_calories)

print("\nАлгоритм динамічного програмування:")
print("Обрані страви:", dp_items)
print("Загальна кількість калорій:", dp_calories)