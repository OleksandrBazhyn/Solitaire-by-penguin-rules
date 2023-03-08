import itertools
import random

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
        
        def __str__(self):
           return str(self.items)
        
        def _show(self, index):
            return self.items[index]

class ReserveColumn:
    def __init__(self, element=None):
        self.element = element

    def set_element(self, element):
        self.element = element

    def get_element(self):
        return self.element
    
    def __str__(self):
           return str(self.element)

class BasicColumn:
    rank = 1
    suit = None

    def __init__(self):
        self.items = []

    def push(self, item):
         if self.card_checking(self, item):
            self.items.append(item)         

    def card_checking(self, item):
        if self.suit == None and item[0]-self.rank == 1:
            self.suit = item[1]
            self.rank = item[0]
            print(f"У цьому базовому стопці ранг: ${self.rank}, а масть: ${self.suit}")
            return True
        elif (item[1] == self.suit) and (item[0]-self.rank == 1):
            self.rank = item[0]
            return True
        else:
            print(f"У цієї карти ранг: ${self.rank}, а масть: ${self.suit}")

    def is_empty(self):
       return len(self.items) == 0

    def size(self):
      return len(self.items)
        
    def __str__(self):
       return str(self.items)
    
    def _show(self, index):
        return self.items[index]

class Game:
    #Пов'язане з картами
    __ranks = []
    __suits = []
    __deck = []

    game_columns = []
    reserve_columns = []
    basic_columns = []

    def __init__(self):
        self.start()

    #Починаємо гру
    def start(self):
        self.create_deck()

        # Створюємо 7 ігрових стопок
        self.game_columns = [GameColumn() for _ in range(7)]

        # Розкладаємо по 7 карт на кожну стопку
        for i in range(7):
            for j in range(7):
                self.game_columns[j].push(self.deck.pop(0))
        
        #Створюємо 7 резервних стопок
        self.reserve_columns = [ReserveColumn() for _ in range(7)]

        #Створюємо 4 базових стопок
        self.basic_columns = [BasicColumn() for _ in range(4)]
        
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