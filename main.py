'''
computer selects a random number 
guess it in the least number of guesses possible
'''
import random
n=random.randint(1,100)
cnt=0
x=int(input("enter guessed number: "))
while(x!=n):
    if(x<n) :
        print("Higher number please")
        cnt+=1
    elif(x>n) :
        print("Lower number please")
        cnt+=1
    x=int(input("enter guessed number: "))

cnt+=1
print(f"you're right and the number of attempts is {cnt}")
