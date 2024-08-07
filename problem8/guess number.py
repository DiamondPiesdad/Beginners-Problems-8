import random
num=random.randint(1,100)
print(num)
t=False
count=1
while t==False:
    ans=int(input())
    if ans==num:
        print("True")
        break
    elif ans>num:
        print("too high")
        count+=1
    else :
        print("too low")
        count+=1
print("you have tried",count,"times")
