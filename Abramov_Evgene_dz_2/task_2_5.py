# task A
prices = [57.8, 46.51, 97, 154.89, 19.36, 32.6, 48, 88.09, 215.18, 199, 112.03, 67.3, 55.7]
format_prices = []
for idx, item in enumerate(prices):
    format_prices.append(f'{int(item)} руб {int(round(item - int(item), 2)*100):02} коп')
print(', '.join(format_prices))

# task B
print(id(prices), prices)
prices.sort()
print(id(prices), prices)

# task C
sorted_prices = sorted(prices, reverse=True)
print(id(sorted_prices), sorted_prices)

# task D
prices.sort()  # можно не писать, т.к. уже есть в task B
print(prices[-5:])
