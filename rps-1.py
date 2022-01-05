import random
b=""
print('\t waepons:- rock paper scissor')
print()
while True:
    c=0
    l=0
    print()
    n=input('enter your weapon: ')
    a=random.randint(1,3)
    if a==1:
        b="rock"
    elif a==2:
        b="paper"
    elif a==3:
        b="scissor"
    print(b)
    if b==n:
        print("draw")
    elif b==n:
        print("draw")
    elif b==n:
        print("draw")
    elif n=="rock":
        if b=="scissor":
            print("win")
        else:
            print("lose")
    elif n=="paper":
        if b=="rock":
            print("win")
        else:
            print("lose")
    elif n=="scissor":
        if b=="paper":
            print("win")
        else:
            print("lose")
    else:
        print("invalid choise of weapon")
    print()
    x=int(input('enter 1 to continue or 0 to stop: '))
    if x==1:
        continue
    else:
        break
