import itertools
import random

# Створюємо список з номіналами карт (2-10, J, Q, K, A)
ranks = [str(num) for num in range(2, 11)] + list('JQKA')

# Створюємо список з мастями (чирва, бубна, креста, піка)
suits = ['чирва', 'бубна', 'трефа', 'піка']

# Створюємо колоду за допомогою функції product() з модуля itertools
deck = list(itertools.product(ranks, suits))

# Тасуємо колоду
random.shuffle(deck)

# Створюємо 7 ігрових стопок
tableau = [[] for _ in range(7)]

# Розкладаємо по 7 карт на кожне стопку
for i in range(7):
    for j in range(7):
        tableau[j].append(deck.pop(0))

# Виводимо стопки на екран
for i in range(7):
    print(f"Стопка {i+1}: {tableau[i]}")

# Виводимо колоду на екран
print("\nКолода:")
for el in deck:
    print(el)