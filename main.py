import solitaire

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
                    print("Неправильно")
                    game_move(game)
            elif move == 2:
                game.RC_to_BC(input("Вкажіть з якої:"), input("Вкажіть в яку:"))
                game_move(game)
            elif move == 3:
                game.deck_to_GC(input("Вкажіть в яку:"))
                game_move(game)
            else:
                print("Неправильно")
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
            print("Неправильно")
            game_move(game)
    except:
        game_move(game)

game = solitaire.Game()
game_move(game)