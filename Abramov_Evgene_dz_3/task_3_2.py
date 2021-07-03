def num_translate(num_eng, diction):
    if num_eng == num_eng.capitalize():
        return diction.setdefault(num_eng.lower()).capitalize()
    else:
        return diction.setdefault(num_eng.lower())


num_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
            'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
num = input('Введите число на английском')
print(num_translate(num, num_dict))
