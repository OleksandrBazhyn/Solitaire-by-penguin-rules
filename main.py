import solitaire

game = solitaire.Game()

game.show_table()

for i in range(1, 7+1):
    game.GC_to_RC(1, i)

game.show_table()


for j in range (1, 4+1):
    game.deck_to_GC(j)
    game.show_table()