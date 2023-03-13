import itertools
import random
import time

def game_move(game):
    try:
        move = int(input("\nВаш хід:\n1 - переставити карту\n2 - показати Правила\n3 - показати стіл\n4 - закінчити гру"))
        if move == 1:
            move = int(input("\nПереставити карту:\n1 - з ігрової стопки\n2 - з резервної стопки в базову\n3 - з запасу в ігрову стопку"))
            if move == 1:
                move = int(input("\nЗ ігрової стопки:\n1 - в ігрову\n2 - в резервну\n3 - в базову"))
                if move == 1:
                    game.GC_to_GC(input("Вкажіть з якої:"), input("Вкажіть в яку:"))
                    game_move(game)
                elif move == 2:
                    game.GC_to_RC(input("Вкажіть з якої:"), input("Вкажіть в яку:"))
                    game_move(game)
                elif move == 3:
                    game.GC_to_BC(input("Вкажіть з якої:"), input("Вкажіть в яку:"))
                    game_move(game)
                else:
                    print("\nНеправильно!")
                    game_move(game)
            elif move == 2:
                game.RC_to_BC(input("Вкажіть з якої:"), input("Вкажіть в яку:"))
                game_move(game)
            elif move == 3:
                game.deck_to_GC(input("Вкажіть в яку:"))
                game_move(game)
            else:
                print("\nНеправильно!")
                game_move(game)
        elif move == 2:
            game.show_rules()
            game_move(game)
        elif move == 3:
            game.show_table()
            game_move(game)
        elif move == 4:
            game.end()
            game_move(game)
        else:
            print("\nНеправильно!")
            game_move(game)
    except:
        game_move(game)

class GameColumn:
        def __init__(self):
            self.items = []
            
        def push(self, item):
            self.items.append(item)
        
        def put_in(self, item):
            self.items.append(item)

        def pop_last_card(self):
            return self.items.pop(-1)

        def is_empty(self):
            return len(self.items) == 0
        
        def __str__(self):
           return str(self.items)
        
        def card_checking(self, item):
            last_card = self.last_card()
            if self.is_empty():
                return True
            elif item[1] == last_card[1] and self.rank_int_value(last_card[0])-self.rank_int_value(item[0]) == 1:
                return True
            else:
                return False
        
        def last_card(self):
            try:
                return self.items[-1]
            except:
                return ValueError

        def rank_int_value(self, rank):
            item_rank = 1
            try:
                item_rank = int(rank)
            except:
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
    
    def pop_element(self):
        card = self.element
        self.element = None
        return card
    
    def __str__(self):
           return str(self.element)
    
    def is_empty(self):
        return self.element == None

class BasicColumn:
    rank = 1
    suit = 'None'

    def __init__(self):
        self.items = []

    def put_in(self, item):
        self.items.clear()
        self.items.append(item)    

    def card_checking(self, item):
        if self.suit == 'None' and self.rank_int_value(item[0])-self.rank == 1:
            self.suit = item[1]
            self.rank = item[0]
            return True
        elif item[1] == self.suit and self.rank_int_value(item[0])-self.rank_int_value(self.rank) == 1:
            self.rank = item[0]
            return True
        else:
            return False

    def rank_int_value(self, rank):
        item_rank = 1
        try:
            item_rank = int(rank)
        except:
            if rank == 'J':
                item_rank = 11
            elif rank == 'Q':
                item_rank = 12
            elif rank == 'K':
                item_rank = 13
            else:
                item_rank = 14
        return item_rank

    def size(self):
      return len(self.items)
        
    def __str__(self):
       return str(self.items)

class Game:
    start_time = None
    deck = []
    game_columns = []
    reserve_columns = []
    basic_columns = []

    def __init__(self):
        self.start()

    #Починаємо гру
    def start(self):
        print()
        self.show_rules()
        self.start_time = time.time()
        self.__create_deck()

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

        self.show_table()
    
    #Створюємо та тасуємо колоду
    def __create_deck(self):
        # Створюємо список з номіналами карт (2-10, J, Q, K, A)
        ranks = [str(num) for num in range(2, 11)] + list('JQKA')

        # Створюємо список з мастями (чирва, бубна, креста, піка)
        suits = ['чирва', 'бубна', 'трефа', 'піка']
        
        # Створюємо колоду за допомогою функції product() з модуля itertools
        self.deck = list(itertools.product(ranks, suits))

        # Тасуємо колоду
        random.shuffle(self.deck)

    def show_table(self):
        if self.__check_win():
            return self.triumph()
        else:
            for i in range(125):
                print("=", end="")
            print("")
            
            # Виводимо резервні стопки на екран
            for i in range(7):
                print(f"Резерв {i+1}: {self.reserve_columns[i]}")
            print()

            # Виводимо ігрові стопки на екран 
            for i in range(7):
                print(f"Стопка {i+1}: {self.game_columns[i]}")

            # Виводимо колоду на екран
            print("\nЗапас:")
            for el in self.deck:
                print(el)
            print()
            
            # Виводимо базові стопки на екран
            for i in range(4):
                print(f"Базова стопка {i+1}: {self.basic_columns[i]}")
    
    def __check_win(self):
        win_str = ''
        for column in range(4):
            win_str += str(self.basic_columns[column].rank)
        if win_str == 'AAAA':
            return True
        else:
            return False

    # Перемога, привітання, закінчення гри
    def triumph(self):
        for i in range(31):
            print("*\\*/", end="")
        print("\n")     

        print("Вітаю, ви перемогли!\n")             

        self.end()
        

    # Гра закінчується, пропонується нова гра
    def end(self):
        for i in range(125):
            print("*", end="")
        print()

        game_time = round((time.time() - self.start_time)/60, 2)
        print(f"Гра тривала {game_time} хв.")

        self.deck = []
        self.game_columns = []
        self.reserve_columns = []
        self.basic_columns = []

        if input("Хочете почати наново? y/n") == 'y':
            self.start()
        else:
            self.end()


    # Ходи
    def GC_to_GC(self, out_path, in_path):
        out_path = int(out_path)
        in_path = int(in_path)
        if (out_path <= 7 and in_path <= 7) and (out_path > 0 and in_path > 0):
            if self.game_columns[out_path - 1].is_empty():
                return ValueError
            elif self.game_columns[in_path - 1].card_checking(self.game_columns[out_path - 1].last_card()):
                self.game_columns[in_path - 1].put_in(self.game_columns[out_path - 1].pop_last_card())
                self.show_table()
            else:
                return ValueError
        else:
            return ValueError
        
    def GC_to_RC(self, out_path, in_path):
        out_path = int(out_path)
        in_path = int(in_path)
        if self.game_columns[out_path - 1].is_empty():
                return ValueError
        elif (out_path <= 7 and in_path <= 7) and (out_path > 0 and in_path > 0):
            if self.reserve_columns[in_path - 1].is_empty():
                self.reserve_columns[in_path - 1].set_element(self.game_columns[out_path - 1].pop_last_card())
                self.show_table()
            else:
                return ValueError
        else:
            return ValueError
        
    def GC_to_BC(self, out_path, in_path):
        out_path = int(out_path)
        in_path = int(in_path)
        if self.game_columns[out_path - 1].is_empty():
                return ValueError
        elif (out_path <= 7 and in_path <= 4) and (out_path > 0 and in_path > 0):
            if self.basic_columns[in_path - 1].card_checking(self.game_columns[out_path - 1].last_card()):
                self.basic_columns[in_path - 1].put_in(self.game_columns[out_path - 1].pop_last_card())
                self.show_table()
            else:
                return ValueError
        else:
            return ValueError
        
    def RC_to_BC(self, out_path, in_path):
        out_path = int(out_path)
        in_path = int(in_path)
        if self.reserve_columns[out_path - 1].is_empty():
                return ValueError
        elif (out_path <= 7 and in_path <= 4) and (out_path > 0 and in_path > 0):
            if self.basic_columns[in_path - 1].card_checking(self.reserve_columns[out_path - 1].get_element()):
                self.basic_columns[in_path - 1].put_in(self.reserve_columns[out_path - 1].pop_element())
                self.show_table()
            else:
                return ValueError
        else:
            return ValueError

    def deck_to_GC(self, in_path):
        in_path = int(in_path)
        if self.deck == []:
                return ValueError
        elif in_path <= 7 and in_path > 0:
            if self.game_columns[in_path - 1].is_empty():
                self.game_columns[in_path - 1].put_in(self.deck.pop(-1))
                self.show_table()
            else:
                return ValueError
        else:
            return ValueError
        
    def show_rules(self):
        with open("author and rules.txt", "r", encoding="utf-8") as rules:
            print(rules.read())
