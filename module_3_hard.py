def calculate_structure_sum(data):
    suma = 0
    for item in data:
        if isinstance(item, (int, float)):
            suma += item
        elif isinstance(item, str):
            suma += len(item)
        elif isinstance(item, (list, tuple, set)):
            suma += calculate_structure_sum(item)
        elif isinstance(item, dict):
            suma += calculate_structure_sum(item.keys())
            suma += calculate_structure_sum(item.values())
    return suma
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)