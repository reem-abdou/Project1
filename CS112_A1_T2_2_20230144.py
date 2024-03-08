#file:CS112_A1_T2_2_20230144
#purpose:played by two players every player will try to collect 3 digits thier sum is 15 and who collects it first will win
#Author:Reem Abdou Mohamed
#ID:20230144
Game = [1,2,3,4,5,6,7,8,9]
sum1 = list([])
sum2 = list([])
print ("welcome to Game!")
print ("Rules: try to collect 3 digits that thier sum is 15")
count = 0
#loop for very turn and when any player wins break loop by count++1
while count == 0 :
  #player1_turn
  print("REMAINING NUMBERS : ")
  print(Game)
  choice = int(input("player1 turn select a number : "))
 #loop that check the input
  while choice not in (Game):
      choice = int(input("select a valid number "))
  Game.remove(choice)
  sum1.append(choice)
  print("NUMBERS OF PLAYER 1 : ")
  print(sum1)
  while len(sum1) >= 3:
    sum=int(sum1[0]) + int(sum1[1]) + int(sum1[2])
    if sum == 15:
      print("PLAYER 1 WINS!!!")
      count=+1
      break   
    elif len(sum1) == 4:
      for x in range (3):
        summ = int(sum - int(sum1[x]) + int(sum1[3]))
        if summ == 15:
           print("PLAYER 1 WINS!!!")
           count=+1
           break
    elif len(sum1) == 5:
      for x in range (3):
        summ = int(sum - int(sum1[x]) + int(sum1[4]))
        if summ == 15:
          print("PLAYER 1 WINS!!!")
          break
        summ = int(sum1[3]) + int(sum1[4]) + int(sum1[x])
        if summ == 15:
          print("PLAYER 1 WINS!!!")
          break
        elif x == 2 :
            print("NO WINNERS PLAY AGAIN")
      count =+ 1
    break
  #player2_turn
  while count == 0 :
    print("REMAINING NUMBERS : ")
    print(Game)
    choice = int(input("player2 turn select a number : "))
    #loop that check the input
    while choice not in (Game):
       choice = int(input("select a valid number "))
    Game.remove(choice)
    sum2.append(choice)
    print("NUMBERS OF PLAYER 2 : ")
    print(sum2)
    while len(sum2) >= 3:
        sum = int(sum2[0]) + int(sum2[1]) + int(sum2[2])
        if sum == 15:
            print("PLAYER 2 WINS!!!")
            count=+1
            break   
        elif len(sum2) == 4:
            for x in range (3):
              summ = int(sum - int(sum2[x]) + int(sum2[3]))
              if summ == 15:
                print("PLAYER 2 WINS!!!")
                count=+1
                break
        break
    break