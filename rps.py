player1=input("enter the value:")
player2=input("enter the value:")
if(player1=="rock" and player2=="scissor"):
    print("player1 wins!!")
elif(player1=="rock" and player2=="paper"):
    print("player2 wins!!")
elif(player1=="paper" and player2=="scissor"):
    print("player2 wins!!")
elif(player1=="paper" and player2=="rock"):
    print("player1 wins!!")
elif(player1=="scissor" and player2=="rock"):
    print("player2 wins!!")
elif(player1=="scissor" and player2=="paper"):
    print("player1 wins!!")
elif(player1==player2):
    print("draw")
else:
    print("invalid")
