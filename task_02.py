# Поиск информативных слов с помощью спискового включения
# Наша цель — решить следующую задачу:
# создать на основе многострочного строкового значения список списков,
# каждый из которых состоит из всех слов одной из строк, причем слова эти длиной три символа и более

text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

w = [[x for x in line.split() if len(x) > 3] for line in text.split('\n')]
print(w)
