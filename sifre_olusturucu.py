import random
chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_length = int(input("How many charcters would you like your password to be?"))
password = ""
for i in range(pass_length):
    password+=random.choice(chars)
print("Your password is: " + password)
