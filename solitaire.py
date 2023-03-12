import itertools
import random

class GameColumn:
        def __init__(self):
            self.items = []
            
        def push(self, item):
            self.items.append(item)
        
        def put_in(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def pop_last_card(self):
            return self.items.pop(-1)

        def is_empty(self):
            return len(self.items) == 0

        def size(self):
            return len(self.items)
        
        def __str__(self):
           return str(self.items)
        
        def card_checking(self, item):
            if self.is_empty():
                return True
            elif item[1] == self.last_card()[1] and self.rank_int_value(self.last_card()[0])-self.rank_int_value(item[0]) == 1:
                return True
            else:
                return False
        
        def last_card(self):
            return self.items[-1]

        def rank_int_value(self, rank):
            item_rank = 1
            try:
                item_rank = int(rank)
            except ValueError:
                if rank == 'J':
                    item_rank = 11
                elif rank == 'Q':
                    item_rank = 12
                elif rank == 'K':
                    item_rank = 13
                else:
                    item_rank = 14
            return item_rank

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
    suit = 'None'

    def __init__(self):
        self.items = []

    def put_in(self, item):
        if self.card_checking(item):
            self.items.clear()
            self.items.append(item)
        else:
            return ValueError         

    def card_checking(self, item):
        if self.suit == 'None' and self.rank_int_value(item[0])-self.rank == 1:
            self.suit = item[1]
            self.rank = item[0]
            return True
        elif item[1] == self.suit and self.rank_int_value(item[0])-self.rank == 1:
            self.rank = item[0]
            return True
        else:
            return False

    def rank_int_value(self, rank):
        item_rank = 1
        try:
            item_rank = int(rank)
        except ValueError:
            if rank == 'J':
                item_rank = 11
            elif rank == 'Q':
                item_rank = 12
            elif rank == 'K':
                item_rank = 13
            else:
                item_rank = 14
        return item_rank

    def is_empty(self):
       return len(self.items) == 0

    def size(self):
      return len(self.items)
        
    def __str__(self):
       return str(self.items)

class Game:
    deck = []
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
        ranks = [str(num) for num in range(2, 11)] + list('JQKA')

        # Створюємо список з мастями (чирва, бубна, креста, піка)
        suits = ['чирва', 'бубна', 'трефа', 'піка']
        
        # Створюємо колоду за допомогою функції product() з модуля itertools
        self.deck = list(itertools.product(ranks, suits))

        # Тасуємо колоду
        random.shuffle(self.deck)

    def show_table(self):
        if self.check_win():
            return self.triumph()
        else:
            # Виводимо резервні стопки на екран
            for i in range(7):
                print(f"Резерв {i+1}: {self.reserve_columns[i]}")

            # Виводимо ігрові стопки на екран
            for i in range(7):
                print(f"Стопка {i+1}: {self.game_columns[i]}")

            # Виводимо колоду на екран
            print("\nКолода:")
            for el in self.deck:
                print(el)

            # Виводимо базові стопки на екран
            for i in range(4):
                print(f"Базова стопка {i+1}: {self.basic_columns[i]}")
            
            for i in range(120):
                print("=", end="")
            print()
    
    def check_win(self):
        win_str = ''
        for column in range(4):
            win_str += str(self.basic_columns[column].rank)
        if win_str == 'AAAA':
            return True
        else:
            return False

    # Перемога, привітання, закінчення гри
    def triumph(self):
        self.end()
    
    # Гра закінчується, пропонується нова гра
    def end(self):
        return KeyError
    
    def GC_to_GC(self, out_path, in_path):
        out_path = int(out_path)
        in_path = int(in_path)
        if self.game_columns[out_path - 1].is_empty():
            return ValueError
        elif self.game_columns[in_path - 1].card_checking(self.game_columns[out_path - 1].last_card()):
            self.game_columns[in_path - 1].put_in(self.game_columns[out_path - 1].pop_last_card())
        else:
            return ValueError