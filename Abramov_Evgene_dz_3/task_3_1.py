def num_translate(num_eng, diction):
    return diction.setdefault(num_eng)


num_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
            'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
num = input('Введите число на английском')
if num == num.capitalize():
    print(num_translate(num.lower(), num_dict).capitalize())
else:
    print(num_translate(num.lower(), num_dict))
