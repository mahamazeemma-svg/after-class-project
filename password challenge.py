import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

password = ""

for i in range(8):
    password += random.choice(letters)
print("Generated password:", password)