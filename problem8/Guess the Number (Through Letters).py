import random
n=random.randint(1,26)
store=str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
letter=store[n+1:n+2]
print(letter)
for i in range(5):
    ans=input()
    if ans==letter:
        print("correct")
        break
    else:
        print("incorrect")