def reverse_kwargs(**kwargs):
    reversed_dict = {}

    for key, value in kwargs.items():
        if not isinstance(key, (int, float, complex, bool, str)):
            key = str(key)
        reversed_dict[value] = key

    return reversed_dict

result = reverse_kwargs(rev=True, acc="YES", stroka=4)
print(result)