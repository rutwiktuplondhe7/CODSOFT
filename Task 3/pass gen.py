import string
import random

def gen_pass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

pass_length = int(input("Enter the desired length of the password: "))

gen_pass = gen_pass(pass_length)

print("Generated password is :", gen_pass)
