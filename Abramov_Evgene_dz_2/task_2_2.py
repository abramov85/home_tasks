message_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(message_list), message_list)
number_of_iterations = len(message_list)
n = 0
while n < number_of_iterations:
    item = message_list.pop(0)
    if item.isdigit():
        message_list.extend(['"', f'{int(item):02}', '"'])
    elif len(item) > 1 and item[1].isdigit():
        message_list.extend(['"', f'{item[:1]}{int(item[1]):02}', '"'])
    else:
        message_list.append(item)
    n += 1
print(id(message_list), message_list)
message = str()
is_opening_mark = True
for idx, item in enumerate(message_list):
    if item.isdigit():
        message += item
    elif len(item) > 1 and item[1].isdigit():
        message += item
    elif item == '"' and is_opening_mark:
        message += item
        is_opening_mark = not is_opening_mark
    elif item == '"':
        message += item + ' '
        is_opening_mark = not is_opening_mark
    elif idx == len(message_list) - 1:
        message += item
    else:
        message += item + ' '
print(message)
