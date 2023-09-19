def find_backpack_combinations(items, max_weight):
    valid_combinations = []
    num_items = len(items)

    def backtrack(current_combination, current_weight, index):
        nonlocal valid_combinations

        if current_weight <= max_weight:
            valid_combinations.append(current_combination)

        for i in range(index, num_items):
            item, weight = items[i]
            new_combination = current_combination + [item]
            new_weight = current_weight + weight
            backtrack(new_combination, new_weight, i + 1)

    backtrack([], 0, 0)

    return valid_combinations

items = {
    'Тент': 10,
    'Спальник': 8,
    'Палатка': 18,
    'Горелка': 3,
    'Гриль': 15,
    'Снаряды для пикника': 5,
    'Фонарик': 1,
    'Каремат': 4,
    'Походная кастрюля': 3,
    'Кружка': 2
}

max_weight = float(input("Введите максимальную грузоподъемность рюкзака в кг: "))
max_weight = max_weight*5 #относительные значения весов брались из расчета, что фонарик, весящий 200 грамм означает "1" по весу в списке

combinations = find_backpack_combinations(list(items.items()), max_weight)

print("Все варианты наборов, не превышающие выбранный вес:")
for combination in combinations:
    print(combination)