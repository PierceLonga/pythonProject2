import random

print(random.randint(0, 1))

print ("choose heads or tails")


choice=input("Enter your choice (heads or tails): ")

num=random.randint(1,2)

if num==1:
    result="heads"

elif num==2:
    result="tails"

if choice==result:
    print("You Win",result)

else:
    print("You Loose")

print("Thanks For Playing")


#Hi Pierce