import random

'''
1 for Rock
-1 for Paper
0 for Seasors
'''

computer=  random.choice([1,-1,0])
yourstr= input("Enter your choice:")
yourdict = {"r":1,"p":-1,"s":0}
reversedict ={1: "Rock",-1:"Paper",0:"Seasors"}

you= yourdict[yourstr]

# Now we have two variables you and computer

print(f"You choose{reversedict[you]}\ncomputer choose{reversedict[computer]} ")

if(computer==you):
    print("Match draw")

else:
    if(computer==1 and you==-1):
        print("You win")  

    elif(computer==-1 and you==1):
        print("computer win")  

    elif(computer==-1 and you==0):
        print("You win")  

    elif(computer==0 and you==-1):
        print("computer win")  

    elif(computer==1 and you==0):
        print("computer win")  

    elif(computer==0 and you==1):
        print("You win")  

    else:
        print("Something went wrong")  