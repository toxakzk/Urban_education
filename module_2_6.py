def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['конь', 67, 76.87]
values_dict = {'a': 'конь', 'b': 67, 'c': 76.87}
print_params(*values_list)
print_params(**values_dict)

