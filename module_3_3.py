def print_params(a=1, b='строка', c=True):
    print(f'a={a}, b={b}, c={c}')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

def print_params(*args, **kwargs):
    print(args)
    print(kwargs)
values_list = [10, 'другая строка', False]
values_dict = {'a': 100, 'b': 'третья строка', 'c': [4, 5]}
print_params(*values_list, **values_dict)


def print_params(a, b, c):
    print(a, f"'{b}'", c)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
