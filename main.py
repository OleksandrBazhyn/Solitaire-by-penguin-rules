import solitaire

game = solitaire.Game()

for i in range(7):
    game.show_table()
    game.GC_to_GC(1, i)