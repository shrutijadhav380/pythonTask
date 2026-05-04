import random
item_list=["rock","paper","scissor"]
user_choice=input("enter your move=rock,paper,scissor:")
comp_choice=random.choice(item_list)

print("userchoice =",user_choice)
print("computer choice=",comp_choice)
if user_choice==comp_choice:
    print("Both choice same mathch tie")
elif user_choice=="rock":
    if comp_choice=="paper":
        print("paper covers rocks =computer win")
    else:
        print("rock smashes scissor=you win")
elif user_choice=="paper":
    if comp_choice=="rock":
        print("paper covers rock=you win")
    else:
        print("scissor cuts paper=computer win")

elif user_choice=="scissor":
    if comp_choice=="rock":
        print("rock smashes scissor=computer win")
    else:
        print("scissor cuts paper=computer win")

else:
    print("invalid choice!please select rock,paper scissor")