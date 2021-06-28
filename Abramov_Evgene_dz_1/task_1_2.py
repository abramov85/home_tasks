list_of_cubes = []
for _num in range(1, 1000, 2):
    cube = _num ** 3
    list_of_cubes.append(cube)

total_sum = 0
for _num in list_of_cubes:
    digit = _num
    digit_sum = 0
    while digit != 0:
        digit_sum += digit % 10
        digit = digit // 10
    if not digit_sum % 7:
        total_sum += _num
print(total_sum)

total_sum = 0
for _num in list_of_cubes:
    num_add_17 = _num + 17
    digit = num_add_17
    digit_sum = 0
    while digit != 0:
        digit_sum += digit % 10
        digit = digit // 10
    if not digit_sum % 7:
        total_sum += num_add_17
print(total_sum)

suma = 0
list = []
for i in range(1, 1001, 2):
    n = i**3
    list.append(n)
# print(list)
for n in list:

    number = n
    sum = 0

    while (number != 0):
        sum += number % 10
        number = number // 10
    # sum += 1
    if sum % 7 == 0:
        suma = suma + n
print(suma)
