duration = int(input('duration: '))
d = duration // 86400
duration = duration % 86400
h = duration // 3600
duration = duration % 3600
m = duration // 60
duration = duration % 60
s = duration

if d > 0:
    print(f'{d} дн {h} час {m} мин {s} сек')
elif h > 0:
    print(f'{h} час {m} мин {s} сек')
elif m > 0:
    print(f'{m} мин {s} сек')
else:
    print(f'{s} сек')
