message_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(message_list), message_list)
number_of_iterations = len(message_list)
n = 0
while n < number_of_iterations:
    message_list.reverse()
    item = message_list.pop()
    if item.isdigit():
        message_list.reverse()
        message_list.append(f'"{int(item):02}"')
        n += 1
    elif len(item) > 1 and item[1].isdigit():
        message_list.reverse()
        message_list.append(f'"{item[:1]}{int(item[1]):02}"')
        n += 1
    else:
        message_list.reverse()
        message_list.append(item)
        n += 1
print(id(message_list), message_list)
print(' '.join(message_list))
