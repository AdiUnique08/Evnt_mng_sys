# Login/Signup for app
# Introduction/Welcoming

# Importing Pandas
import pandas as pd


def login():
    while True:
        print("\n\n\n\tLogin as:\n\t1. Admin\n\t2. Student")
        user_inp_2 = input("\tChoose (Enter number): ")

        if user_inp_2 == '1':  # Login as admin
            # Assigning Userpass_Adm Sheet to New var
            userpass_adm_xl = pd.read_excel(userpass, 'Admins')

            # Username:User_infos as key:value pair
            user_infos = list(zip(userpass_adm_xl.PASSWORDS, userpass_adm_xl.NAME,
                                  userpass_adm_xl.T_NT, userpass_adm_xl.ROLE, userpass_adm_xl.POST,
                                  userpass_adm_xl.EMAIL))
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
                    print("\tDo you want to login as a Student or Signup?\n\tYou'll be taken to the login page")
                    break

                if i == 5:
                    print("\tYou've entered the wrong credentials 5 times")
                    print("\tPlease wait for 30 seconds")
                    break
            break

        elif user_inp_2 == '2':  # Login as student
            # Assigning Userpass_Std Sheet to New var
            userpass_std_xl = pd.read_excel(userpass, 'Students')

            # Usernames : Password as key value pair
            user_infos = list(zip(userpass_std_xl.PASSWORDS, userpass_std_xl.NAME,
                                  userpass_std_xl.CLASS, userpass_std_xl.SEC, userpass_std_xl.ROLE,
                                  userpass_std_xl.EMAIL))
            userpass_std = dict(zip(userpass_std_xl.USERNAMES, user_infos))

            # Variable to control the no. of times user can keep entering wrong password
            i = 0

            while i < 5:  # Initiating loop for logging in
                username = input("\n\n\n\tUsername: ")
                password = input("\tPassword: ")

                # Executes if proper credentials were entered.
                if username in userpass_std and password == userpass_std[username][0]:
                    print("\tThank you")
                    print("\tYou will be shortly taken to the main page")
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

        # Executes when invalid number has been entered
        elif user_inp_2 != '1' or user_inp_2 != '2':
            print("\tEnter a Valid Number")
            continue


def signup():
    while True:
        print("\n\n\n\tSignup as:\n\t1. Admin\n\t2. Student")
        user_inp_2 = input("\tChoose (Enter number): ")

        # Signup as admin
        if user_inp_2 == '1':
            # Assigning Userpass_Adm Sheet to New var
            userpass_adm_xl = pd.read_excel(userpass, 'Admins')

            # Individually putting data into their respective lists
            username_adm = list(userpass_adm_xl.USERNAMES)
            password_adm = list(userpass_adm_xl.PASSWORDS)
            name_adm = list(userpass_adm_xl.NAME)
            t_nt_adm = list(userpass_adm_xl.T_NT)
            role_adm = list(userpass_adm_xl.ROLE)
            post_adm = list(userpass_adm_xl.POST)
            email_adm = list(userpass_adm_xl.EMAIL)

            # Taking Information related to user
            username = input("\n\n\n\tUsername: ")

            # Checking if username already exists in userpass_std
            if username in username_adm:
                print("\tUsername already exists")
                print("\tYou'll be taken to the Login page")
                input("\tPress Enter to continue")
                break

            # Loop to ensure Valid password is entered
            # Loop to endure any error in password can be corrected without proceeding further
            while True:
                password = input("\tPassword: ")
                # Checking whether password consists of letter and digits
                if password.isalnum() == True:
                    if password.isalpha() == False and password.isdigit() == False:
                        print("\tValid username and password")
                        print("\tYou'll be taken further")
                        input("\tPress Enter to continue")
                        break

                    elif password.isalpha() == False and password.isdigit() == True:
                        print("\tPassword doesn't consist of letters")
                        print("\tPlease add letter a-z or A-Z")
                        continue

                    elif password.isalpha() == True and password.isdigit() == False:
                        print("\tPassword doesn't consist of numbers")
                        print("\tPlease add numbers from 0-9")
                        continue

            # Taking Inputs as first name and last name and individually holding checks
            while True:
                f_name = input("\n\n\tFirst Name: ")
                l_name = input("\tLast Name: ")

                # Ensuring user has entered or typed their names correctly
                print("\n\t1. Proceed (No error)\n\t2. Repeat (Error)")
                user_inp_4 = input("\tChoose (Enter number): ")

                # Executes if user has no errors in their name
                if user_inp_4 == '1':

                    # Checking first name
                    if f_name.isalpha() == True:
                        if f_name[0].isupper() == True:
                            name = f_name + ' '
                        else:
                            name = f_name.capitalize() + ' '

                    # Checking last name
                    if l_name.isalpha() == True:
                        if l_name[0].isupper() == True:
                            name += l_name
                        else:
                            name += l_name.capitalize()
                    break

                # Executes if the user has incorrectly entered their names
                elif user_inp_4 == '2':
                    continue

                else:
                    continue

            print("\n\t1. Teaching\n\t2. Non-Teaching")
            user_inp_3 = int(input("\tChoose (Enter number): "))

            if user_inp_3 == '1':
                t_nt = 'Teaching'
                role = 'Admin'
                post = input("\tPost: ")

            elif user_inp_3 == '2':
                t_nt = 'Non_Teaching'
                role = 'Admin'
                post = input("\tPost: ")

            elif user_inp_3 != '1' or user_inp_3 != '2':
                print("Enter your info again")
                continue

            email = input("\tEmail: ")

            # Appending new values entered to lists
            username_adm.append(username)
            password_adm.append(password)
            name_adm.append(name)
            t_nt_adm.append(t_nt)
            role_adm.append(role)
            post_adm.append(post)
            email_adm.append(email)

            # Creating Dataframe of appended lists
            user_info_adm = pd.DataFrame(list(zip(username_adm, password_adm, name_adm,
                                                  t_nt_adm, role_adm, post_adm, email_adm)),
                                         columns=['USERNAMES', 'PASSWORDS', 'NAME',
                                                  'T_NT', 'ROLE', 'POST', 'EMAIL'])

            # Transferring updated df to Excel sheet = 'Admins'
            with pd.ExcelWriter(r'C:\Users\97150\OneDrive\Desktop\Accounts_Info.xlsx', engine='openpyxl', mode='a',
                                if_sheet_exists='replace') as writer:
                user_info_adm.to_excel(writer, sheet_name='Admins')

            print("\n\n\n\tThank you for signing up")
            print("\tYou will be taken to the login page\n\n\n")
            break

        # Signup as Student
        elif user_inp_2 == '2':
            # Assigning Userpass_Adm Sheet to New var
            userpass_std_xl = pd.read_excel(userpass, 'Students')

            # Individually putting data into their respective lists
            username_std = list(userpass_std_xl.USERNAMES)
            password_std = list(userpass_std_xl.PASSWORDS)
            name_std = list(userpass_std_xl.NAME)
            clss_std = list(userpass_std_xl.CLASS)
            sec_std = list(userpass_std_xl.SEC)
            role_std = list(userpass_std_xl.ROLE)
            email_std = list(userpass_std_xl.EMAIL)

            # Taking Information related to user
            # Loop to endure any error in password can be corrected without proceeding further
            username = input("\n\n\n\tUsername: ")

            # Checking if username already exists in userpass_std
            if username in username_std:
                print("\tUsername already exists")
                print("\tYou'll be taken to the Login page")
                input("\tPress Enter to continue")
                break

            # Loop to ensure Valid password is entered
            while True:
                password = input("\tPassword: ")
                # Checking whether password consists of letter and digits
                if password.isalnum() == True:
                    if password.isalpha() == False and password.isdigit() == False:
                        print("\tValid username and password")
                        print("\tYou'll be taken further")
                        input("\tPress Enter to continue")
                        break

                    elif password.isalpha() == False and password.isdigit() == True:
                        print("\tPassword doesn't consist of letters")
                        print("\tPlease add letter a-z or A-Z")
                        continue

                    elif password.isalpha() == True and password.isdigit() == False:
                        print("\tPassword doesn't consist of numbers")
                        print("\tPlease add numbers from 0-9")
                        continue

            # Taking Inputs as first name and last name and individually holding checks
            while True:
                f_name = input("\n\n\tFirst Name: ")
                l_name = input("\tLast Name: ")

                # Ensuring user has entered or typed their names correctly
                print("\n\t1. Proceed (No error)\n\t2. Repeat (Error)")
                user_inp_4 = input("\tChoose (Enter number): ")

                # Executes if user has no errors in their name
                if user_inp_4 == '1':

                    # Checking first name
                    if f_name.isalpha() == True:
                        if f_name[0].isupper() == True:
                            name = f_name + ' '
                        else:
                            name = f_name.capitalize() + ' '

                    # Checking last name
                    if l_name.isalpha() == True:
                        if l_name[0].isupper() == True:
                            name += l_name
                        else:
                            name += l_name.capitalize()
                    break

                # Executes if the user has incorrectly entered their names
                elif user_inp_4 == '2':
                    continue

                else:
                    continue

            clss = int(input("\n\tClass (Numbers only): "))
            sec = input("\tSection (Capital letters only): ")
            role = 'Student'
            email = input("\tEmail: ")

            # Appending new values entered to the lists
            username_std.append(username)
            password_std.append(password)
            name_std.append(name)
            clss_std.append(clss)
            sec_std.append(sec)
            role_std.append(role)
            email_std.append(email)

            # Creating Dataframe of the appended lists
            user_info_std = pd.DataFrame(list(zip(username_std, password_std, name_std,
                                                   clss_std, sec_std, role_std, email_std)),
                                          columns=['USERNAMES', 'PASSWORDS', 'NAME', 'CLASS',
                                                   'SEC', 'ROLE', 'EMAIL'])

            # Transferring updated df to Excel sheet = 'Students'
            with pd.ExcelWriter(r'C:\Users\97150\OneDrive\Desktop\Accounts_Info.xlsx', engine='openpyxl', mode='a',
                                if_sheet_exists='replace') as writer:
                user_info_std.to_excel(writer, sheet_name='Students')

            print("\n\n\n\tThank you for signing up")
            print("\tYou will be taken to the login page\n\n\n")
            break

        elif user_inp_2 != '1' or user_inp_2 != '2':
            print("\tEnter a Valid Number")
            continue


# Actual Program
print("---------Welcome to Event Management System---------")

while True:
    print("\t1. Login\n\t2. Signup")
    user_inp_1 = int(input("\tChoose (Enter number): "))

    # Obtaining Excel file containing Usernames and passwords
    userpass = pd.ExcelFile(r'C:\Users\97150\OneDrive\Desktop\Accounts_Info.xlsx')
    user_info = []

    if user_inp_1 == 1:
        login()
        break

    elif user_inp_1 == 2:
        signup()

del userpass
