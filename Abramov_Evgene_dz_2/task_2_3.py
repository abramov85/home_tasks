message_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
message = str()
for idx, item in enumerate(message_list):
    if item.isdigit():
        message += f'"{int(item):02}" '
    elif len(item) > 1 and item[1].isdigit():
        message += f'"{item[:1]}{int(item[1]):02}" '
    elif idx == len(message_list) - 1:
        message += item
    else:
        message += item + ' '
print(message)

