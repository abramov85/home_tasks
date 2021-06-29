list_of_employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                     'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for idx, item in enumerate(list_of_employees):
    next_to_lsat_space_index = len(item) - item[::-1].index(' ')
    print('Привет, ' + item[next_to_lsat_space_index:].title())
