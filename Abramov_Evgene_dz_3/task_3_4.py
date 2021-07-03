def thesaurus(*names):
    name_thesaurus = {}
    for item in names:
        if name_thesaurus.get(item[0]) is None:
            name_thesaurus.setdefault(item[0], [item])
        else:
            name_thesaurus[item[0]] += [item]
    return name_thesaurus


def thesaurus_adv(*args):
    last_name_thesaurus = {}
    for item in args:
        full_name = item.split(' ')
        if last_name_thesaurus.get(full_name[-1][0]) is None:
            last_name_thesaurus.setdefault(full_name[-1][0], [item])
        else:
            last_name_thesaurus[full_name[-1][0]] += [item]
    for key, val in last_name_thesaurus.items():
        last_name_thesaurus[key] = thesaurus(*val)
    print(last_name_thesaurus)


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
