def find_duplicates(elements):
  seen = set()
  result = set()

  for element in elements:
    if element in seen:
      result.add(element)
    else:
      seen.add(element)

  return list(result)

user_input = input("Введите элементы списка (через пробел): ")
user_elements = user_input.split()

user_elements = [int(element) for element in user_elements]

duplicates = find_duplicates(user_elements)
print("Повторяющиеся элементы:", duplicates)