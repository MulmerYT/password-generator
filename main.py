import random
caract = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
long = int( input("¿Cuántos carácteres?") )

for i in range(long):
    password += random.choice(caract)
print(password)
