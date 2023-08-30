##Листинг 2.4. Однострочное решение, помечающее строковые значения,
# содержащие строку символов 'anonymous'
txt = ['lambda functions are anonymous functions.',
       'anonymous functions dont have a name.',
       'functions are objects in Python.']
## Однострочник
mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)
## Результаты
print(list(mark))
