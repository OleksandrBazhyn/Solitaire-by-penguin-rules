import itertools
import random

class Game:
    #Пов'язане з картами
    __ranks = []
    __suits = []
    __deck = []

    class GameColumn:
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def is_empty(self):
            return len(self.items) == 0

        def size(self):
            return len(self.items)
        
    column = GameColumn()

    def __init__(self):
        self.start()

    #Починаємо гру
    def start(self):
        self.create_deck()

        # Створюємо 7 ігрових стопок
        self.column = [[] for _ in range(7)]

        # Розкладаємо по 7 карт на кожну стопку
        for i in range(7):
            for j in range(7):
                self.column[j].append(self.deck.pop(0))
        
    #Створюємо та тасуємо колоду
    def create_deck(self):
        # Створюємо список з номіналами карт (2-10, J, Q, K, A)
        self.ranks = [str(num) for num in range(2, 11)] + list('JQKA')

        # Створюємо список з мастями (чирва, бубна, креста, піка)
        self.suits = ['чирва', 'бубна', 'трефа', 'піка']
        
        # Створюємо колоду за допомогою функції product() з модуля itertools
        self.deck = list(itertools.product(self.ranks, self.suits))

        # Тасуємо колоду
        random.shuffle(self.deck)

game = Game()

# Виводимо стопки на екран
for i in range(7):
    print(f"Стопка {i+1}: {game.column[i]}")

# Виводимо колоду на екран
print("\nКолода:")
for el in game.deck:
    print(el)