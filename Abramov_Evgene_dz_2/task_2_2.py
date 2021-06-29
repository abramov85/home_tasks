# message_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# edited_message_list = []
# for idx, item in enumerate(message_list):
#     if item.isdigit():
#         edited_message_list.append(f'"{int(item):02}"')
#     elif len(item) > 1 and item[1].isdigit():
#         edited_message_list.append(f'"{item[:1]}{int(item[1]):02}"')
#     else:
#         edited_message_list.append(item)
# print(edited_message_list)
# print(' '.join(edited_message_list))

message_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(message_list), message_list)
for idx, item in enumerate(message_list):
    if item.isdigit():
        message_list[idx] = f'"{int(item):02}"'
    elif len(item) > 1 and item[1].isdigit():
        message_list[idx] = f'"{item[:1]}{int(item[1]):02}"'
print(id(message_list), message_list)
print(' '.join(message_list))
