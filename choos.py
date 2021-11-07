name = input("type your name: ")
print("welcome ", name, " to this adventure" )

answer = input("you areona dirt road, it has come to an end and yo ou can gleft or right.wich way would you like to go? " ).lower() 
 

if answer == "left":
    answer=input("you come to a river,you can walk around it or swim across? type walk towalk arounnd and swim accross: ")

    if answer == "swim":
        print("you swam across and were eaten by an alli gator.")
    elif answer == "walk":    
        print("you walk for many miles, ran out of water and you lost the game.")
    else:
        print("not a valid  option. you lose.")

elif answer == "right":
    print("you come to brige,it looks wobbly,do you wan to cross itor head back(cross/back)?")
else:
    print("not a valid option.you lose.")  