# Нужно найти всех сотрудников, зарабатывающих по крайней мере 100 000 долларов в год
employees = {'Alice': 10000,
             'Bob': 99817,
             'Carol': 1229087,
             'Frank': 88123,
             'Eve': 93121}
# top_earners = []
# for key, val in employees.items():
#     if val >= 100000:
#         top_earners.append((key, val))
# print(top_earners)

print([(key,val) for key, val in employees.items() if val >= 100000])
