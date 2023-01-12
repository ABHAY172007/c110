import random
dice=input("do you want to roll a dice press Y")
response="y"
while response=="y":
    no=random.randint(1,6)
    if no==1:
        print("the number of dice is 1")
    if no==2:
        print("the number of dice is 2")
    if no==3:
        print("the number of dice is 3")
    if no==4:
        print("the number of dice is 4")
    if no==5:
        print("the number of dice is 5")
    if no==6:
        print("the number of dice is 6")
    print("\n")






