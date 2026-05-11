import numpy as np

# Створюємо одновимірний масив з 200 випадкових чисел від -100 до 100
array = np.random.randint(-100, 101, 200)

print("Початковий масив:")
print(array)

# Використовуємо маску для фільтрації додатніх чисел
positive_mask = array > 0
positive_numbers = array[positive_mask]

print("\nДодатні числа:")
print(positive_numbers)

# Замінюємо всі від’ємні значення на 0
array[array < 0] = 0

print("\nМасив після заміни від’ємних чисел на 0:")
print(array)

# Обчислюємо середнє значення нового масиву
mean_value = array.mean()

print("\nСереднє значення масиву:", mean_value)
