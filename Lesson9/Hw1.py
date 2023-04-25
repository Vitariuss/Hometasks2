import pandas as pd

data = pd.read_csv("C:/Users/Vit/Desktop/Python/Lesson9/sample_data/california_housing_train.csv")
filtered_data = data.loc[(data['population'] >= 0) & (data['population'] <= 500)]
average_house_price = filtered_data['median_house_value'].mean()

print("Средняя стоимость дома, где количество людей от 0 до 500: ", average_house_price)