for i in range(21):
    if i in [1]:
        percent = 'процент'
    elif i in [2, 3, 4]:
        percent = 'процента'
    else:
        percent = 'процентов'
    print(f'{i} {percent}')
