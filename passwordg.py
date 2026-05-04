import random 
import string

lenght=int(input("enter a password lenght:"))

char=string.ascii_letters+string.digits+string.punctuation

password=""
for i in range(lenght):
    password+=random.choice(char)

print("generated password:",password)