password=str(input())
score=0
if len(password)>=7:
    score+=1

for letter in password:
    if letter.isupper()==True:
        score+=1
        break

for letter in password:
    if letter.islower()==True:
        score+=1
        break

for letter in password:
    if letter.isdigit()==True:
        score+=1
        break

for letter in password:
    if letter.isalnum()==False:
        score+=1
        break

print(score)
if score==5:
    print("strong")
elif score>=4:
    print("moderately strong")
else:
    print("weak")