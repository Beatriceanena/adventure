name=input("Enter your name")
print("welcome" , name ,"to this adenture")

answer=input ("You are on a dirt road, it has come to an end which way would you like to go, right or left ")
 
if answer == "left":
    answer= input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim around:")
    if answer == "swim":
        print('You swam across and were eaten by an alligator')
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
         print("not a valid option you lose")  
if answer == "right":
    answer= input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    if answer == "back":
        print("You go back and loose")
    elif answer == "cross":
        answer= input("You cross the bridge and meet stranger.Do you talk to them (yes/no)")
        if answer == "yes":
            print("You talk to the stranger and they give you gold")
        if answer == "no":
            print("You ignore the stranger and he gets offended and you loose")  
    else:
         print("not a valid option you lose")

else:
    print("not a valid option you lose")
