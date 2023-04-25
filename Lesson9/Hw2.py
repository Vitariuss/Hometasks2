import pandas as pd

data = pd.read_csv("C:/Users/Vit/Desktop/Python/Lesson9/sample_data/california_housing_train.csv")

min_population = data['population'].min()

min_population_data = data[data['population'] == min_population]

max_households = min_population_data['households'].max()

print(f"Максимальное количество households в зоне с минимальным значением population ({min_population}) равно {max_households}")