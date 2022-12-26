# Login/Signup for app
# Introduction/Welcoming


# Importing Pandas, Time
import pandas as pd

global user_info


def login():
    while True:
        print("\n\n\n\tLogin as:\n\t1. Admin\n\t2. Student")
        user_inp_2 = int(input("\tChoose (Enter number): "))

        if user_inp_2 == 1:  # Login as admin
            # Assigning Userpass_Adm Sheet to New var
            userpass_adm_xl = pd.read_excel(userpass, 'Userpass_Adm')

            # Username:User_infos as key:value pair
            user_infos = list(zip(userpass_adm_xl.PASSWORDS, userpass_adm_xl.NAME,
                                  userpass_adm_xl.T_NT, userpass_adm_xl.ROLE, userpass_adm_xl.POST))
            userpass_adm = dict(zip(userpass_adm_xl.USERNAMES, user_infos))

            # Variable to control the no. of times user can keep entering wrong password
            i = 0

            while i < 5:  # Initiating loop for logging in
                username = input("\n\n\n\tUsername: ")
                password = input("\tPassword: ")

                # Executes if proper credentials were entered.
                if username in userpass_adm and password == userpass_adm[username][0]:
                    print("\tThank you")
                    print("\tYou will shortly be taken to the main page")
                    user_info = [username]
                    for i in userpass_adm[username]:
                        user_info.append(i)
                    break

                elif username in userpass_adm and password != userpass_adm[username][0]:
                    print("\tInvalid password\n\tPlease enter again")
                    i += 1

                elif username not in userpass_adm:
                    print("\tUsername is not found in Admin")
                    print("\tDo you want to login as a Student?\n\tYou'll be taken to the login page")
                    break

                if i == 5:
                    print("\tYou've entered the wrong credentials 5 times")
                    print("\tPlease wait for 30 seconds")
                    break
            break

        elif user_inp_2 == 2: # Login as student
            # Assigning Userpass_Std Sheet to New var
            userpass_std_xl = pd.read_excel(userpass, 'Userpass_Std')

            # Usernames : Password as key value pair
            user_infos = list(zip(userpass_std_xl.PASSWORDS, userpass_std_xl.NAME,
                                  userpass_std_xl.CLASS, userpass_std_xl.SEC, userpass_std_xl.ROLE))
            userpass_std = dict(zip(userpass_std_xl.USERNAMES, user_infos))

            # Variable to control the no. of times user can keep entering wrong password
            i = 0

            while i < 5:  # Initiating loop for logging in
                username = input("\n\n\n\tUsername: ")
                password = input("\tPassword: ")

                # Executes if proper credentials were entered.
                if username in userpass_std and password == userpass_std[username][0]:
                    print("\tThank you\n\tYou will shortly be taken to the main page")
                    print("\tYou'll be shortly taken to the main page")
                    user_info = [username]
                    for i in userpass_std[username]:
                        user_info.append(i)
                    break

                elif username in userpass_std and password != userpass_std[username][0]:
                    print("\tInvalid password\n\tPlease enter again")
                    i += 1

                elif username not in userpass_std:
                    print("\tUsername is not found in Students")
                    print("\tDo you want to login as an Admin?\n\tYou'll be taken to the login page")
                    break

                if i == 5:
                    print("\tYou've entered the wrong credentials 5 times")
                    print("\tPlease wait for 30 seconds")
                    break
            break

        elif user_inp_2 <1 or user_inp_2 > 2:
            print("\tEnter a valid number")


def signup_adm():
    pass


def signup_std():
    pass


# Actual Program

print("---------Welcome to Event Management System---------")


while True:
    print("\t1. Login\n\t2. Signup")
    user_inp_1 = int(input("\tChoose (Enter number): "))

    # Obtaining Excel file containing Usernames and passwords
    userpass = pd.ExcelFile(r'C:\Users\97150\PycharmProjects\Event_Mng_Sys\Account_Signin.xlsx')

    if user_inp_1 == 1:
        login()
        break

    elif user_inp_1 == 2:
        while True:
            print("\n\n\n\tSignup as:\n\t1. Admin\n\t2. Student")
            user_inp_2 = int(input("\tChoose (Enter number): "))

            if user_inp_2 == 1:  # Signup as admin

                # Assigning Userpass_Adm Sheet to New var
                userpass_adm_xl = pd.read_excel(userpass, 'Userpass_Adm')

                # Username:User_infos as key:value pair
                user_infos = list(zip(userpass_adm_xl.PASSWORDS, userpass_adm_xl.NAME,
                                      userpass_adm_xl.T_NT, userpass_adm_xl.ROLE, userpass_adm_xl.POST))
                userpass_adm = dict(zip(userpass_adm_xl.USERNAMES, user_infos))

                # Taking Information related to user
                username = input("\n\n\n\tUsername: ")
                password = input("\tPassword: ")

                if username in userpass_adm:
                    print("\tUsername already exists")
                    print("\tYou'll be taken to the Login page")

                name = input("\tName: ")
                print("\t1. Teaching\n\t2. Non-Teaching")
                user_inp_3 = int(input("\tChoose (Enter number): "))

                if user_inp_3 == 1:
                    t_nt = 'Teaching'
                    role = 'Admin'
                    post = input("\tPost: ")

                elif user_inp_3 == 2:
                    t_nt = 'Non_Teaching'
                    role = 'Admin'
                    post = input("\tPost: ")

                elif user_inp_3 < 1 or user_inp_3 > 2:
                    print("Enter your info again")

                user_info_new = [password, name, t_nt, role, post]

                userpass_adm_upd = dict(zip(username, user_info_new))
                userpass_adm.update(userpass_adm_upd)
                userpass_adm = pd.DataFrame(userpass_adm)
                with pd.ExcelWriter(r'C:\Users\97150\PycharmProjects\Event_Mng_Sys\Account_Signin.xlsx') as writer:
                    userpass_adm.to_excel(writer, sheet_name='Userpass_Adm')

                print("\n\n\n\tThank you for signing up")
                print("\tYou will be taken to the login page")
                break

            elif user_inp_2 == 2:  # Signup as student
                login_std()
                break
del userpass