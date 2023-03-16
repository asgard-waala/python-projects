def main():
    print("Welcome to the email slicer!" + "\n")
    
    email_input = input("Enter your email address: ")

    username, domain = email_input.split("@")
    domain, extension = domain.split(".")

    print("This is your username: ", username)
    print("This is your domain: ", domain)
    print("This is the extenstion you are using: ", extension)

while True:
    main()
