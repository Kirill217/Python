" Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык."

num_translate = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eght': 'восемь',
    'nine': 'девять'
}

def translate_numbers(num_dict):
    return num_translate.get(num_dict)

print(translate_numbers('five'))