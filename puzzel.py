import random
n=5
tbg=int(n*random.random())+1
guess=0
while guess!= tbg:
    guess=int(input("new guess no:"))
    if guess>0:
        if guess>tbg:
            print("number to large")
        elif guess<tbg:
            print("number too small")
else:
    print("Congrtulation you done")