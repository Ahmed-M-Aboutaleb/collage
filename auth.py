from uuid import uuid4
from os import path, makedirs

db = 'database/users'

# valid() - validate the user inputs
# The function will check if the name, email, password and role are not empty
# The function will check if the role is f or c
# The function will return True if the inputs are not valid
# name - the user name
# email - the user email
# password - the user password
# role - the user role

def valid(name, email, password, role):
    if name == "" or email == "" or password == "" or role == "":
        print("❌ | All fields are required")
        return True
    if role != "f" and role != "c":
        print("❌ | Invalid role")
        return True
    return False
    

# login() - login the user
# The function will ask the user to enter the name and password
# The function will check if the user exists
# The function will check if the password is correct
# The function will return the user name and role
# it will return the user name and role as a list

def login():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    if(name == "" or password == ""):
        print("❌ | All fields are required")
        return login()
    if not path.exists(f'{db}/{name}'):
        print('❌ | User not found')
        return login()
    fileName = f"{db}/{name}/{name}.txt"
    userFile = open(fileName)
    user = userFile.readlines()
    passwordFromDb = user[3].split("\n")[0]
    role = user[4].split("\n")[0]
    if password == passwordFromDb:
        print(f"👋 | Welcome {name}")
        return [name, role]
    else:
        print("❌ | Wrong Password")
        return login()

# signup() - signup the user
# The function will ask the user to enter the name, email, password and role
# The function will check if the user inputs are valid
# The function will check if the user already exists
# The function will create a new user
# The function will return the user name and role

def signup():
    id = uuid4()
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    role = input("Enter your role (f for freelancer, c for client): ")
    if valid(name, email, password, role):
        return signup()
    if role == "f":
        phone = input("Enter your phone number: ")
        national = input("Enter your national id: ")
        if phone == "" or national == "":
            print("❌ | All fields are required")
            return signup()
    if not path.exists(db):
        makedirs(db)
    fileName = f"{db}/{name}/{name}.txt"
    if path.exists(f"{db}/{name}"):
        print("❌ | User already exists")
        return signup()
    else:
        makedirs(f"{db}/{name}")
    userFile = open(fileName, 'w')
    userFile.write(f"{id}\n{name}\n{email}\n{password}\n{role}\n")
    if role == "f":
        userFile.write(f"{phone}\n{national}")
        userFile.close()
        fileName = f"{db}/freelancers.txt"
        if not path.exists(fileName):
            freelancersFile = open(fileName, "w")
            freelancersFile.write(name+"\n")
            freelancersFile.close()
        else:
            freelancersFile = open(fileName, "a")
            freelancersFile.write(name +"\n")
            freelancersFile.close()
    else:
        userFile.close()
    print("✅ | Signup done")
    return False