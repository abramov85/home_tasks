def thesaurus(*names):
    name_thesaurus = {}
    for item in names:
        if name_thesaurus.get(item[0]) is None:
            name_thesaurus.setdefault(item[0], [item])
        else:
            name_thesaurus[item[0]] += [item]
    print(name_thesaurus)


thesaurus('Иван', 'Сергей', 'Виктор', 'Илья', 'Денис', 'Станислав', 'Игнат')
