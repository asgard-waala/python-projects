import string
import random

characters = list(
    string.ascii_letters + string.digits + """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
)


def generate_password():
    password_length = int(input("Enter the length of password?: "))
    random.shuffle(characters)
    password = []
    for i in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = "".join(password)
    print(password)


option = input("Do you want to generate a random password? (Yes/No): ").lower()
if option == "yes":
    generate_password()
else:
    print(" We only accept Yes or No. Thank you!")
    quit()
