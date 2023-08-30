# Однострочное решение для поиска в тексте последовательностей символов и их непосредственного окружения
letters_amazon = '''
We spent several years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as
the commercial engines, but at one-tenth of the cost. We were
not surprised when this worked.
'''
## Однострочник
find = lambda x, q: x[x.find(q)-18:x.find(q)+18] if q in x else -1
## Результат
print(find(letters_amazon, 'SQL'))