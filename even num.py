def num(l):
    odd_list = []
    for n in l:
        if n % 2 != 0:
            odd_list.append(n)
    return odd_list

print(num([5,10,15,20]))

'''def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))'''
