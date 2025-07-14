import random # random module which helps to choose the random number between 1,-1,0
computer = random.choice([1,-1,0])#here how we define it

youstr=input("Enter your choice:-").strip().upper()#users input in S,s,G,g,W,w

yourdict={"S":1,"W":-1,"G":0}#Dictionary which save the string with the numbers
reversedict={1:"SNAKE",-1:"WATER",0:"GUN"}#this is dictionary which saves the number with the string like REVERSE of the dic1

you=yourdict[youstr] # here we have a"you"name variable which helps to store the key-value pair between the input and created dictionary

print(f"You chose:-{reversedict[you]} \nComputer chose:-{reversedict[computer]} ")#Here we show whom choos to who

if(computer == you):
    print("***TIE***")
else:
    if (computer == 1 and you == -1):
        print("***You lose***")
    elif(computer == -1 and you == 0):
        print("***You lose***")
    elif(computer == 0 and you == 1):
        print("***You lose***")
    elif (computer == -1 and you == 1):
        print("***You Win***")
    elif(computer == 0 and you == -1):
        print("***You Win***")
    elif(computer == 1 and you == 0):
        print("***You Win***")
    else:
        print("! SOMETHING WENT WRONG !")