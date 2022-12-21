import auth
import client
import freelaner

# main() - the main function
# The function will ask the user to login or signup
# The function will call the login() or signup() function from auth.py
# The function will call the main() function from client.py or freelaner.py
# based on the user role

def main():
    option = input("(1) Login \n(2) signup \n")
    if option == "1":
        [name, role] = auth.login()
        if role == 'f':
            freelaner.main(name)
        else:
            client.main(name)
    elif option == "2":
        auth.signup()
    else:
        print("❌ | Invalid option")

main()