# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

phrase_vinny = input('Винни-Пух введи фразу: ')
list_words_in_phrase = phrase_vinny.split()
vowels = 'аеёиоуыэюя'

def count_letters_vowels(word: str):
    count = 0
    for k in word:
        if k in vowels:
           count += 1
    return count
    
count_vowels = list(map(count_letters_vowels, list_words_in_phrase))


if len(set(count_vowels)) > 1:
    print('“Пам парам”')
else:
    print('“Парам пам-пам”')

