from random import choice


def get_jokes(number_of_jokes, repeat_flag):
    """

    :param number_of_jokes: max number of jokes in without repeating mode limited by № of words in list
    :param repeat_flag: if 1 then allows repeating
    :return:
    """
    if repeat_flag == 1:
        for i in range(number_of_jokes):
            print(f'{choice(nouns)} '
                  f'{choice(adverbs)} '
                  f'{choice(adjectives)}')
    else:
        if number_of_jokes > min(len(nouns), len(adverbs), len(adjectives)):
            number_of_jokes = min(len(nouns), len(adverbs), len(adjectives))
        for i in range(number_of_jokes):
            print(f'{nouns.pop(nouns.index(choice(nouns)))} '
                  f'{adverbs.pop(adverbs.index(choice(adverbs)))} '
                  f'{adjectives.pop(adjectives.index(choice(adjectives)))}')


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
get_jokes(9, 0)
