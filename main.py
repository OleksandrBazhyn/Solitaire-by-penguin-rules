import solitaire as Game

game = Game.Game()

# Виводимо резервні стопки на екран
for i in range(7):
    print(f"Резерв {i+1}: {game.reserve_columns[i]}")

# Виводимо ігрові стопки на екран
for i in range(7):
    print(f"Стопка {i+1}: {game.game_columns[i]}")

# Виводимо колоду на екран
print("\nКолода:")
for el in game.deck:
    print(el)

game.basic_columns[0].push(game.game_columns[0]._show(2))