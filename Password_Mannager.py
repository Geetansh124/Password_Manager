import random
import string

passwords = {}

#load existing file
try:
    with open("ppasswords.txxt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd
except:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%&"
    password = ''.join(random.choice(chars) for _ in range(8))
    return password

while True:
    print("\n-----PASSWORD MANAGER APP-----")
    print("1. Save Password")
    print("2. View Password")
    print("3. Generate Password")
    print("4. Exit")

    choice = input("Enter Your Choice:")

    if choice == "1":
        site = input("Enter Your Website: ")
        pwd = input("Enter Your Password: ")

        passwords[site] = pwd
        with open("Password.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")

        print("Password Saved")

    elif choice == "2":
        if not passwords:
            print("No Password Avaliable")

        else:
            for site , pwd in passwords.items():
                print(site,":", pwd)
    elif choice == "3":
        print("Generated Password", generate_password())
    elif choice == "4":
        print("Ok Bye..")
        break
    else:
        print("Invalid Input!")

