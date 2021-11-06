import random
roshambo = ["r","p","s"]
cpick = (random.choice(roshambo))
pick = input("enter you choice (R)ock, (P)aper, (S)cissors")
print (cpick)
print (pick)
if pick is "r" and cpick is "s":
    print ("rock beats scissors! you win")
elif pick =="r" and cpick == "P":
    print("paper covers rock you lose")
elif pick =="r" and cpick == "r":
    print("it's a tie")
elif pick =="p" and cpick == "r":    
    print("paper beats rock you win!")
elif pick =="p" and cpick == "s":    
    print("scissors beats paper you lose!")
elif pick =="p" and cpick == "p":    
    print("it's a tie")
elif pick =="s" and cpick == "p":    
    print("scissors beats paper you win!")
elif pick =="s" and cpick == "r":    
    print("rock beats scissors you lose!")
elif pick =="s" and cpick == "s":    
    print("it's a tie")