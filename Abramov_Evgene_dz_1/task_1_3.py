for _i in range(21):
    if _i in [1]:
        percent = 'процент'
    elif _i in [2, 3, 4]:
        percent = 'процента'
    else:
        percent = 'процентов'
    print(f'{_i} {percent}')
