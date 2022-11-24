# Testing for working of login/signup

a = 1
while a == 1:
    print("\t\tWelcome to <App_name>")
    print("\tWould you like to Login or Signup? (1/2)")
    user_inp_1 = int(input("\t"))
    for i in range(4):

        if user_inp_1 == 1:
            print("\tLogin [Admin(1) or Student(2)]")
            user_inp_2 = int(input("\t"))

            if user_inp_2 == 1:
                userpass_adm = {'Bhavani': 'Bhavani@1234', 'Shyamsundar': 'Shyam@1234', 'Vranda': 'Vra@1234'}
                userpass_adm.update(userpass_adm_new)
                del username, password
                username = input("Username: ")
                password = input("Password: ")

                if username in userpass_adm and password == userpass_adm[username]:
                    print("\t\tThank You!\n\tYou'll be taken to the main page")

                    if username in userpass_adm:
                        user_info = {username: [password, 'Admin']}
                        print(user_info)
                        a = 0
                        break

                elif username in userpass_adm and password != userpass_adm[username]:
                    print("Invalid username or password\nPlease enter again")
                    user_inp_2 = 1

                elif username not in userpass_adm:
                    print("Username doesn't exist in Admin\nLogin as student or Signup")
                    break

            elif user_inp_2 == 2:
                userpass_std = {'Aditya': 'Adi@1234', 'Prateek': 'Peek@1234', 'Sudhiksha': 'Seek@1234',
                                'Nihal': "Nexacon1234"}
                userpass_std.update(userpass_std_new)
                del username, password
                username = input("Username: ")
                password = input("Password: ")

                if username in userpass_std and password == userpass_std[username]:
                    print("\t\tThankyou \n\tYou'll be taken to the main page")

                    if username in userpass_std:
                        user_info = {username: [password, 'Student']}
                        print(user_info)
                        a = 0
                        break

                elif username in userpass_std and password != userpass_std[username]:
                    print("Invalid username or password\nPlease enter again")
                    user_inp_2 = 2

                elif username not in userpass_std:
                    print("Username doesn't exist in Student\nLogin as admin or Signup")
                    break

        elif user_inp_1 == 2:
            print("\t\tSignup [Admin(1) or Student(2)]")
            user_inp_2 = int(input("\t"))

            if user_inp_2 == 1:
                userpass_adm = {'Bhavani': 'Bhavani@1234', 'Shyamsundar': 'Shyam@1234', 'Vranda': 'Vra@1234'}
                print("Enter the following details")
                username = input("Username: ")
                password = input("Password: ")
                userpass_adm_new = {username: password}

                user_inp_3 = input("Continue? ")
                name = input("Name: ")
                email = input("Email ID: ")
                subj_list = []
                for j in range(3):
                    Subj = input("Subjects (Enter 1 at a time): ")
                    subj_list.append(Subj)
                user_inp_4 = input("Continue? ")
                print("Thank you for signing up\nYou'll be taken to the login page")
                user_info_adv = [name, email, 'Admin'].extend(subj_list)
                print(user_info_adv)
                break

            elif user_inp_2 == 2:
                userpass_std = {'Aditya': 'Adi@1234', 'Prateek': 'Peek@1234', 'Sudhiksha': 'Seek@1234',
                                'Nihal': "Nexacon1234"}
                username = input("Userame: ")
                password = input("Password: ")
                userpass_std_new = {username: password}

                user_inp_3 = input("Continue? ")
                name = input("Name: ")
                clss = input("Class: ")
                sec = input("Section: ")
                email = input("Email ID: ")
                user_inp_4 = input("Continue? ")
                print("Thank You for signing up\nYou'll be taken to the Login page")
                user_info_adv = [name, clss, sec, email, 'Student']
                break

if user_inp_1 == 1:
    if user_inp_2 == 1:
        print("\t\tMain Page (Admin)")
    elif user_inp_2 == 2:
        print("\t\tMain Page (Student)")
print("\t\tWelcome <name>")
