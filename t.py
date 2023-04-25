from ortools.sat.python import cp_model

# Определяем константы
NUM_WORKERS = 8
NUM_SHIFTS = 2
DAYS_IN_WEEK = 7
MAX_CONSECUTIVE_WORK_DAYS = 5

# Определяем данные для каждого работника
workers_data = [
    {"id": 1, "name": "Иван", "shift_preferences": [(0, 0), (1, 1)], "day_off_preferences": [2, 3], "max_shifts": 6},
    {"id": 2, "name": "Петр", "shift_preferences": [(0, 1), (1, 0)], "day_off_preferences": [], "min_shifts": 4},
    {"id": 3, "name": "Ольга", "shift_preferences": [(0, 0), (1, 0)], "day_off_preferences": [3, 4], "max_shifts": 5},
    {"id": 4, "name": "Мария", "shift_preferences": [(0, 1), (1, 1)], "day_off_preferences": [], "min_shifts": 4},
    {"id": 5, "name": "Андрей", "shift_preferences": [(0, 0), (0, 1)], "day_off_preferences": [], "min_shifts": 5},
    {"id": 6, "name": "Николай", "shift_preferences": [(1, 0), (1, 1)], "day_off_preferences": [5], "max_shifts": 6},
    {"id": 7, "name": "Елена", "shift_preferences": [(0, 1), (1, 0)], "day_off_preferences": [], "min_shifts": 4},
    {"id": 8, "name": "Дмитрий", "shift_preferences": [(0, 0), (1, 1)], "day_off_preferences": [], "max_shifts": 5},
]

# Определяем модель
model = cp_model.CpModel()

# Определяем переменные
shifts = {}
for i in range(NUM_WORKERS):
    for j in range(NUM_SHIFTS):
        for k in range(DAYS_IN_WEEK):
            shifts[(i, j, k)] = model.NewBoolVar("shifts[%i,%i,%i]" % (i, j, k))

# Определяем ограничения
for i in range(NUM_WORKERS):
    # Ограничения на количество смен
    if "min_shifts" in workers_data[i]:
        min_shifts = workers_data[i]["min_shifts"]
        model.Add(sum(shifts[(i, j, k)] for j in range(NUM_SHIFTS) for k in range(DAYS_IN_WEEK)) >= min_shifts)
    if "max_shifts" in workers_data[i]:
        max_shifts = workers_data[i]["max_shifts"]
        model.Add(sum(shifts[(i, j, k)] for j in range(NUM_SHIFTS) for k in range(DAYS_IN_WEEK)) <= max_shifts)
    # Ограничения на дни отдыха
    day_off_preferences = workers_data[i]["day_off_preferences"]
    for day_off in day_off_preferences:
        for j in range(NUM_SHIFTS):
            model.Add(shifts[(i, j, day_off)] == 0)
    # Ограничения на пожелания по сменам
    shift_preferences = workers_data[i]["shift_preferences"]
    for shift_preference in shift_preferences:
        model.Add(shifts[(i, shift_preference[0], shift_preference[1])] == 1)
    # Ограничения на переработку
    for j in range(NUM_SHIFTS):
        for k in range(DAYS_IN_WEEK - MAX_CONSECUTIVE_WORK_DAYS):
            consecutive_shifts = sum(shifts[(i, j, k + l)] for l in range(MAX_CONSECUTIVE_WORK_DAYS))
            model.Add(consecutive_shifts <= MAX_CONSECUTIVE_WORK_DAYS)

# Определяем целевую функцию
objective = sum(shifts[(i, j, k)] for i in range(NUM_WORKERS) for j in range(NUM_SHIFTS) for k in range(DAYS_IN_WEEK))
model.Maximize(objective)

# Решаем задачу
solver = cp_model.CpSolver()
status = solver.Solve(model)

# Выводим результаты
if status == cp_model.OPTIMAL:
    for i in range(NUM_WORKERS):
        print("Работник %s:" % workers_data[i]["name"])
        for j in range(NUM_SHIFTS):
            for k in range(DAYS_IN_WEEK):
                if solver.Value(shifts[(i, j, k)]) == 1:
                    shift = "утро" if j == 0 else "вечер"
                    print("    %s, %s" % (shift, k))
else:
    print("Решение не найдено.")