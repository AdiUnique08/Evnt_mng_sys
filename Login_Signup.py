# Login/Signup for app
# Introduction/Welcoming

# Importing Pandas and time
import pandas as pd
import time


def login():
    while True:
        print("\n\n\n\tLogin as:\n\t1. Admin\n\t2. Student")
        user_inp_2 = input("\tChoose (Enter number): ")

        # Login as admin
        time.sleep(2)
        if user_inp_2 == '1':
            # Assigning Userpass_Adm Sheet to New var
            userpass_adm_xl = pd.read_excel(userpass, 'Admins')

            # Username:User_infos as key:value pair
            user_infos = list(zip(userpass_adm_xl.PASSWORDS, userpass_adm_xl.NAME,
                                  userpass_adm_xl.T_NT, userpass_adm_xl.ROLE, userpass_adm_xl.POST,
                                  userpass_adm_xl.EMAIL))
            userpass_adm = dict(zip(userpass_adm_xl.USERNAMES, user_infos))

            # Variable to control the no. of times user can keep entering wrong password
            i = 0
            j = 0

            while i < 5:  # Initiating loop for logging in
                username = input("\n\n\n\tUsername: ")
                password = input("\tPassword: ")
                user_inp_3 = input("\tConfirm to proceed (Y/N): ")

                if (user_inp_3.upper() == 'Y') or (user_inp_3.capitalize() == 'Yes'):

                    # Executes if proper credentials were entered.
                    time.sleep(2)
                    if username in userpass_adm:
                        if password == userpass_adm[username][0]:
                            print("\tThank you")
                            time.sleep(2)
                            print("\tYou will shortly be taken to the main page")
                            user_info = [username]
                            for i in userpass_adm[username]:
                                user_info.append(i)
                            break

                        elif password != userpass_adm[username][0]:
                            print("\tInvalid username or password\n\tPlease enter again")
                            i += 1

                    elif username not in userpass_adm:
                        if j < 3:
                            time.sleep(1)
                            print("\tInvalid username entered")
                            print("\tPlease enter again")
                            j += 1
                            continue
                        else:
                            time.sleep(1)
                            print("\tUsername not found in Admin")
                            print("\tYou will be taken to the Login/Signup page")
                            j = 0
                            break

                    if i == 5:
                        time.sleep(1)
                        print("\tYou've entered the wrong credentials 5 times")
                        print("\tPlease wait for 30 seconds")
                        time.sleep(30)
                        i = 0
                        continue

                elif (user_inp_3.upper() == 'N') or (user_inp_3.capitalize() == 'No'):
                    continue

                else:
                    time.sleep(1)
                    print("\tEnter a valid option")
                    print("\tEnter your info. again")
                    continue

                # Breaking from loop if successfully passed the checking
                if (username == user_info[0]) and (password == user_info[1]):
                    break

#-----------------------------------------------------------------------------------------------------------------------

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
            j = 0

            while i < 5:  # Initiating loop for logging in
                username = input("\n\n\n\tUsername: ")
                password = input("\tPassword: ")
                user_inp_3 = input("\tConfirm to proceed (Y/N): ")

                if (user_inp_3.upper() == 'Y') or (user_inp_3.capitalize() == 'Yes'):

                    # Executes if proper credentials were entered.
                    time.sleep(2)
                    if username in userpass_std:
                        if password == userpass_std[username][0]:
                            print("\tThank you")
                            time.sleep(2)
                            print("\tYou will shortly be taken to the main page")
                            user_info = [username]
                            for i in userpass_std[username]:
                                user_info.append(i)
                            break

                        elif password != userpass_std[username][0]:
                            print("\tInvalid username or password\n\tPlease enter again")
                            i += 1

                    elif username not in userpass_std:
                        if j < 3:
                            time.sleep(1)
                            print("\tInvalid username entered")
                            print("\tPlease enter again")
                            j += 1
                            continue
                        else:
                            time.sleep(1)
                            print("\tUsername not found in Student")
                            print("\tYou will be taken to the Login/Signup page")
                            j = 0
                            break

                    if i == 5:
                        time.sleep(1)
                        print("\tYou've entered the wrong credentials 5 times")
                        print("\tPlease wait for 30 seconds")
                        time.sleep(30)
                        i = 0
                        continue

                elif (user_inp_3.upper() == 'N') or (user_inp_3.capitalize() == 'No'):
                    continue

                else:
                    time.sleep(1)
                    print("\tEnter a valid option")
                    print("\tEnter your info. again")
                    continue

                # Breaking from loop if successfully passed the checking
                if (username == user_info[0]) and (password == user_info[1]):
                    break


#-----------------------------------------------------------------------------------------------------------------------

        # Executes when invalid number has been entered
        elif user_inp_2 != '1' or user_inp_2 != '2':
            print("\tEnter a Valid Number")
            continue


def signup():
    while True:
        print("\n\n\n\tSignup as:\n\t1. Admin\n\t2. Student")
        user_inp_2 = input("\tChoose (Enter number): ")

        # Signup as admin
        time.sleep(2)
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

            # List of special characters to ensure password consists of them
            spec_ch = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',
                       '[', ']', '{', '}', ';', ':', '<', '>', '/', '\\', '|', ' ']

            # Taking Information related to user
            username = input("\n\n\n\tUsername: ")

            # Checking if username already exists in userpass_std
            if username in username_adm:
                print("\tUsername already exists")
                print("\tYou'll be taken to the Login page")
                input("\tPress Enter to continue")
                break

            # Loop to ensure Valid password is entered
            while True:
                print("\tPassword must consist of the following:")
                print("\t1. 8-20 Characters long")
                print("\t2. Consist of letters A-Z and a-z")
                print("\t3. Consist of digits 0-9")
                print("\t4. Consist of any special characters")
                password = input("\tPassword: ")

                # Parameter to count the no. of special characters
                count = 0

                # Checks if password consists of the minimum characters
                if (len(password) >= 8) and (len(password) <= 20):

                    # Checking whether password consists of letter and digits
                    if password.isalnum() is False:
                        if (password.isalpha() is False) and (password.isdigit() is False):

                            # Checking whether password consists of special characters:
                            for i in password:
                                if i in spec_ch:
                                    count += 1
                                    if i == password[len(password) - 1]:
                                        break
                                    else:
                                        continue
                                else:
                                    continue

                            # Setting timer of 2 seconds before the checking starts
                            time.sleep(2)

                            # Checking if special characters did exist or not
                            if count > 0:
                                print("\tValid username and password")
                                print("\tYou'll be taken further")
                                input("\tPress Enter to continue")
                                break
                            else:
                                print("\tPassword doesn't consist of any special characters.")
                                print("\tPlease add a special character")
                                continue

                        elif (password.isalpha() is False) and (password.isdigit() is True):
                            print("\tPassword doesn't consist of letters")
                            print("\tPlease add letter a-z or A-Z")
                            continue

                        elif (password.isalpha() is True) and (password.isdigit() is False):
                            print("\tPassword doesn't consist of numbers")
                            print("\tPlease add numbers from 0-9")
                            continue
                else:
                    print("\tPassword must consist of 8-20 characters")
                    continue

            # Taking Inputs as first name and last name and individually holding checks
            while True:
                time.sleep(2)
                f_name = input("\n\n\tFirst Name: ")
                l_name = input("\tLast Name: ")

                # Ensuring user has entered or typed their names correctly
                time.sleep(1)
                print("\n\t1. Proceed (No error)\n\t2. Repeat (Error)")
                user_inp_3 = input("\tChoose (Enter number): ")

                # Executes if user has no errors in their name
                time.sleep(2)
                if user_inp_3 == '1':

                    # Checking first name
                    if f_name.isalpha() is True:
                        if f_name[0].isupper() is True:
                            name = f_name + ' '
                        else:
                            name = f_name.capitalize() + ' '

                    # Checking last name
                    if l_name.isalpha() is True:
                        if l_name[0].isupper() is True:
                            name += l_name
                        else:
                            name += l_name.capitalize()
                    break

                # Executes if the user has incorrectly entered their names
                elif user_inp_3 == '2':
                    continue

                else:
                    print("Enter a valid number")
                    continue

            time.sleep(2)
            print("\n\t1. Teaching\n\t2. Non-Teaching")
            user_inp_4 = input("\tChoose (Enter number): ")

            time.sleep(1)
            if user_inp_4 == '1':
                t_nt = 'Teaching'
                role = 'Admin'
                post = input("\tPost: ")

            elif user_inp_4 == '2':
                t_nt = 'Non_Teaching'
                role = 'Admin'
                post = input("\tPost: ")

            elif user_inp_4 != '1' or user_inp_4 != '2':
                print("Enter your info again")
                continue

            # Taking Email as input
            while True:
                time.sleep(1)
                print("\tCurrently accepting only emails with the following domains:")
                print("\t1. @gmail.com")
                print("\t2. @hotmail.com")
                print("\t3. @yahoo.com")
                email = input("\tEmail: ")

                # Checking whether email entered consists of a valid domain or not
                if (email.endswith("@gmail.com") or
                        email.endswith("@hotmail.com") or
                        email.endswith("@yahoo.com")):
                    print("\tValid Email")
                    break
                else:
                    print("\tInvalid Email")
                    continue

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
            with pd.ExcelWriter(root, engine='openpyxl', if_sheet_exists='overlay', mode='a') as writer:
                user_info_adm.to_excel(writer, sheet_name='Admins')

            time.sleep(1)
            print("\n\n\n\tThank you for signing up")
            time.sleep(2)
            print("\tYou will be taken to the login page\n\n\n")
            time.sleep(2)
            break

#-----------------------------------------------------------------------------------------------------------------------

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

            # List of special characters to ensure password consists of them
            spec_ch = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',
                       '[', ']', '{', '}', ';', ':', '<', '>', '/', '\\', '|', ' ']

            # Taking Information related to user
            username = input("\n\n\n\tUsername: ")

            # Checking if username already exists in userpass_std
            if username in username_std:
                print("\tUsername already exists")
                print("\tYou'll be taken to the Login page")
                input("\tPress Enter to continue")
                break

            # Loop to ensure Valid password is entered
            while True:
                print("Password must consist of the following:")
                print("\t1. 8-20 Characters long")
                print("\t2. Consist of letters A-Z and a-z")
                print("\t3. Consist of digits 0-9")
                print("\t4. Consist of any special characters")
                password = input("\tPassword: ")

                # Parameter to count the no. of special characters
                count = 0

                # Checks if password consists of the minimum characters
                if (len(password) >= 8) and (len(password) <= 20):

                    # Checking whether password consists of letter and digits
                    if password.isalnum() is False:
                        if (password.isalpha() is False) and (password.isdigit() is False):

                            # Checking whether password consists of special characters:
                            for i in password:
                                if i in spec_ch:
                                    count += 1
                                    if i == password[len(password) - 1]:
                                        break
                                    else:
                                        continue
                                else:
                                    continue

                            # Setting timer of 2 seconds before the checking starts
                            time.sleep(2)

                            # Checking if special characters did exist or not
                            if count > 0:
                                print("\tValid username and password")
                                print("\tYou'll be taken further")
                                input("\tPress Enter to continue")
                                break
                            else:
                                print("\tPassword doesn't consist of any special characters.")
                                print("\tPlease add a special character")
                                continue

                        elif (password.isalpha() is False) and (password.isdigit() is True):
                            print("\tPassword doesn't consist of letters")
                            print("\tPlease add letter a-z or A-Z")
                            continue

                        elif (password.isalpha() is True) and (password.isdigit() is False):
                            print("\tPassword doesn't consist of numbers")
                            print("\tPlease add numbers from 0-9")
                            continue
                else:
                    print("\tPassword must consist of 8-20 characters")
                    continue

            # Taking Inputs as first name and last name and individually holding checks
            while True:
                time.sleep(2)
                f_name = input("\n\n\tFirst Name: ")
                l_name = input("\tLast Name: ")

                # Ensuring user has entered or typed their names correctly
                time.sleep(1)
                print("\n\t1. Proceed (No error)\n\t2. Repeat (Error)")
                user_inp_3 = input("\tChoose (Enter number): ")

                # Executes if user has no errors in their name
                time.sleep(2)
                if user_inp_3 == '1':

                    # Checking first name
                    if f_name.isalpha() is True:
                        if f_name[0].isupper() is True:
                            name = f_name + ' '
                        else:
                            name = f_name.capitalize() + ' '

                    # Checking last name
                    if l_name.isalpha() is True:
                        if l_name[0].isupper() is True:
                            name += l_name
                        else:
                            name += l_name.capitalize()
                    break

                # Executes if the user has incorrectly entered their names
                elif user_inp_3 == '2':
                    continue

                else:
                    print("Enter a valid number")
                    continue

            time.sleep(2)
            clss = int(input("\n\tClass (Numbers only): "))
            sec = input("\tSection (Capital letters only): ")
            role = 'Student'

            # Taking Email as input
            time.sleep(1)
            while True:
                print("\tCurrently accepting only emails with the following domains:")
                print("\t1. @gmail.com")
                print("\t2. @hotmail.com")
                print("\t3. @yahoo.com")
                email = input("\tEmail: ")

                # Checking whether email entered consists of a valid domain or not
                if (email.endswith("@gmail.com") or
                        email.endswith("@hotmail.com") or
                        email.endswith("@yahoo.com")):
                    print("\tValid Email")
                    break
                else:
                    print("\tInvalid Email")
                    continue

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
            with pd.ExcelWriter(root, engine='openpyxl', if_sheet_exists='overlay', mode='a') as writer:
                user_info_std.to_excel(writer, sheet_name='Students')

            time.sleep(1)
            print("\n\n\n\tThank you for signing up")
            time.sleep(2)
            print("\tYou will be taken to the login page\n\n\n")
            time.sleep(2)
            break

#-----------------------------------------------------------------------------------------------------------------------

        elif user_inp_2 != '1' or user_inp_2 != '2':
            print("\tEnter a Valid Number")
            continue


# Actual Program
print("---------Welcome to Event Management System---------")

while True:
    print("\t1. Login\n\t2. Signup")
    user_inp_1 = input("\tChoose (Enter number): ")

    # Assigning path of file to a variable
    root = r"C:\Users\97150\PycharmProjects\Event_Mng_Sys\Account_Signin.xlsx"

    # Obtaining Excel file containing Usernames and passwords
    userpass = pd.ExcelFile(root)
    user_info = []

    if user_inp_1 == '1':
        login()
        break

    elif user_inp_1 == '2':
        signup()

    else:
        print("Enter a Valid Option: ")
        continue

del userpass
