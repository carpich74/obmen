print("С играем в Крестики-нолики для двух игроков ?")

print("Начнем?")
field = list(range(1,10))
def draw_field(field):
   print("_" * 15)
   for i in range(3):
      print("||", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "||")
      print("-" * 15)

# выбираем количество игроков
# def choose_players():
#     players = input("Выберите количество игроков: 1 или 2? ")
#     if players == "1":
#         print("Вы выбрали игру с компьютером")
#     elif players == "2":
#         print("Вы выбрали игру с другим игроком")
#     else:
#         # print("Выберите 1 или 2")
#         return players
#
# choose_players()
# выбираем символы для игроков
def choose_symbols():
    player1 = input("Выберите символ для игрока 1: X или O? ")
    if player1 == "X":
        player2 = "O"
    elif player1 == "O":
        player2 = "X"
    else:
        print("Выберите X или O")

    print("Игрок 1 играет за", player1)
    print("Игрок 2 играет за", player2)
choose_symbols()


def take_input(player_symbol):
   valid = False
   while not valid:
       player_answer = input('Выберите цифру для постановки ' + player_symbol+'? ')
       try:
           player_answer = int(player_answer)
       except:
           print("Вы уверены, что ввели число?")
           continue
       if player_answer >= 1 and player_answer <= 9:
         if(str(field[player_answer-1]) not in "XO"):
            field[player_answer-1] = player_symbol
            valid = True
         else:
            print("Эта клетка уже занята!")
       else:
        print("Введите число от 1 до 9.")

# вводим победные комбинации символов

def check_win(field):
   win_value = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_value:
      if field[each[0]] == field[each[1]] == field[each[2]]:
         return field[each[0]]
   return False

# основная функция игры
def main(field):
   counter = 0
   win = False
   while not win:
      draw_field(field)
      if counter % 2 == 0:
         take_input("X")
      else:
         take_input("O")
      counter += 1
      if counter > 4:
         tmp = check_win(field)
         if tmp:
            print(tmp, "выиграл!")
            win = True
            break
      if counter == 9:
         print("Ничья!")
         break
main(field)
input("Нажмите Enter для выхода!")
