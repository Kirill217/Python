# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых
# из трёх списков (по одному из каждого):
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(word):
    joke = []
    for i in range(word):
        joke_nouns = random.choice(nouns)
        joke_adverbs = random.choice(adverbs)
        joke_adjectives = random.choice(adjectives)
        # joke.append() = f'{joke_nouns}, {joke_adjectives}, {joke_adverbs}'
        joke.append(f'{joke_nouns}, {joke_adjectives}, {joke_adverbs}')
        return joke

print(get_jokes(1))
# до меня долго доходило что в  функцию нужно записать число