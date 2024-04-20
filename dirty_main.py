from package.module import *  # импорт всего что в нем есть
with open('dirty_main.py', 'w') as file:
file.write('def add(a, b):\n')
file.write('    return a + b\n\n')


file.write('def subtract(a, b):\n')
file.write('    return a - b\n\n')

file.write('def multiply(a, b):\n')
file.write('    return a * b\n\n')


print(add(5, 3))  # Выведет 8
print(subtract(10, 4))  # Выведет 6
print(multiply(2, 7))  # Выведет 14

# Этот код создает файл dirty_main.py и записывает туда три функции: add, subtract и multiply,
# которые выполняют операции сложения, вычитания и умножения.
# Затем код импортирует все функции из модуля package.module, который включает в себя эти же функции add, subtract и multiply.
# Далее вызываются эти три функции с различными аргументами и их результаты выводятся на экран.