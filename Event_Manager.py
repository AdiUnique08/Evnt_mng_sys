# Login/Signup for app
# Introduction/Welcoming

# Importing Pandas and time
import pandas as pd
import time
import random as r

global root, userpass, userpass_adm_xl, userpass_std_xl
global user_info, user_id
global username_adm, password_adm, ids_adm, name_adm, t_nt_adm, role_adm, post_adm, email_adm
global username_std, password_std, ids_std, name_std, clss_std, sec_std, role_std, email_std
global role, username, password, name, t_nt, post, email
global clss, sec
global check


def obtain_data_adm():
    global userpass_adm_xl
    global username_adm, password_adm, ids_adm, name_adm, t_nt_adm, role_adm, post_adm, email_adm

    # Assigning Userpass_Adm Sheet to New var
    userpass_adm_xl = pd.read_excel(userpass, 'Admins')

    # Individually putting data into their respective lists
    username_adm = list(userpass_adm_xl.USERNAMES)
    password_adm = list(userpass_adm_xl.PASSWORDS)
    ids_adm = list(userpass_adm_xl.USER_IDS)
    name_adm = list(userpass_adm_xl.NAME)
    t_nt_adm = list(userpass_adm_xl.T_NT)
    role_adm = list(userpass_adm_xl.ROLE)
    post_adm = list(userpass_adm_xl.POST)
    email_adm = list(userpass_adm_xl.EMAIL)


def obtain_data_std():
    global userpass_std_xl
    global username_std, password_std, ids_std, name_std, clss_std, sec_std, role_std, email_std

    # Assigning Userpass_Std Sheet to New var
    userpass_std_xl = pd.read_excel(userpass, 'Students')

    # Individually putting data into their respective lists
    username_std = list(userpass_std_xl.USERNAMES)
    password_std = list(userpass_std_xl.PASSWORDS)
    ids_std = list(userpass_std_xl.USER_IDS)
    name_std = list(userpass_std_xl.NAME)
    clss_std = list(userpass_std_xl.CLASS)
    sec_std = list(userpass_std_xl.SEC)
    role_std = list(userpass_std_xl.ROLE)
    email_std = list(userpass_std_xl.EMAIL)


def transfer_data_adm():
    # Creating Dataframe of appended lists
    user_info_adm = pd.DataFrame(list(zip(username_adm, password_adm, ids_adm, name_adm,
                                          t_nt_adm, role_adm, post_adm, email_adm)),
                                 columns=['USERNAMES', 'PASSWORDS', 'USER_IDS', 'NAME',
                                          'T_NT', 'ROLE', 'POST', 'EMAIL'])

    # Transferring updated df to Excel sheet = 'Admins'
    with pd.ExcelWriter(root, engine='openpyxl', if_sheet_exists='overlay', mode='a') as writer:
        user_info_adm.to_excel(writer, sheet_name='Admins')


def transfer_data_std():
    # Creating Dataframe of the appended lists
    user_info_std = pd.DataFrame(list(zip(username_std, password_std, ids_std, name_std,
                                          clss_std, sec_std, role_std, email_std)),
                                 columns=['USERNAMES', 'PASSWORDS', 'USER_IDS', 'NAME', 'CLASS',
                                          'SEC', 'ROLE', 'EMAIL'])

    # Transferring updated df to Excel sheet = 'Students'
    with pd.ExcelWriter(root, engine='openpyxl', if_sheet_exists='overlay', mode='a') as writer:
        user_info_std.to_excel(writer, sheet_name='Students')


def password_check():
    global check
    while True:
        # List of special characters to ensure password consists of them
        spec_ch = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',
                   '[', ']', '{', '}', ';', ':', '<', '>', '/', '\\', '|', ' ', '.', ',',
                   '?', '|']

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
                        print("\tValid password")
                        print("\tYou'll be taken further")
                        input("\tPress Enter to continue")
                        check = 'Successful'
                        break
                    else:
                        print("\tPassword doesn't consist of any special characters.")
                        print("\tPlease add a special character")
                        check = 'Unsuccessful'
                        break

                elif (password.isalpha() is False) and (password.isdigit() is True):
                    print("\tPassword doesn't consist of letters")
                    print("\tPlease add letter a-z or A-Z")
                    check = 'Unsuccessful'
                    break

                elif (password.isalpha() is True) and (password.isdigit() is False):
                    print("\tPassword doesn't consist of numbers")
                    print("\tPlease add numbers from 0-9")
                    check = 'Unsuccessful'
                    break

            else:
                print("\tPassword consists of Letters and Digits with no separation")
                print("\tPlease add whitespaces (space) between letters and digits")
                check = 'Unsuccessful'
                break

        else:
            print("\tPassword must consist of 8-20 characters")
            check = 'Unsuccessful'
            break


def assign_values():
    global role, username, password, name, t_nt, post, email
    global clss, sec
    # Values
    role = user_info[user_id][6]
    # Assigning values to respective variables depending on role of user
    if role == 'Admin':
        username = user_info[user_id][0]
        password = user_info[user_id][1]
        name = user_info[user_id][2]
        t_nt = user_info[user_id][3]
        post = user_info[user_id][4]
        email = user_info[user_id][5]

    elif role == 'Student':
        username = user_info[user_id][0]
        password = user_info[user_id][1]
        name = user_info[user_id][2]
        clss = user_info[user_id][3]
        sec = user_info[user_id][4]
        email = user_info[user_id][5]


def login():
    global userpass, check
    while True:
        global user_info, user_id
        print("\n\n\n\t---------LOGIN---------")
        print("\n\tLogin as:\n\t1. Admin\n\t2. Student")
        user_inp_2 = input("\tChoose (Enter number): ")

        # Login as admin
        time.sleep(2)
        if user_inp_2 == '1':
            print("\n\n\n\t---------LOGIN(ADMIN)---------")

            # Assigning Userpass_Adm Sheet to New var
            userpass_adm_xl = pd.read_excel(userpass, 'Admins')

            # Username:User_infos as key:value pair
            user_infos = list(zip(userpass_adm_xl.PASSWORDS, userpass_adm_xl.USER_IDS,
                                  userpass_adm_xl.NAME, userpass_adm_xl.T_NT,
                                  userpass_adm_xl.POST, userpass_adm_xl.EMAIL,
                                  userpass_adm_xl.ROLE))
            userpass_adm = dict(zip(userpass_adm_xl.USERNAMES, user_infos))

            # Variable to control the no. of times user can keep entering wrong password
            i = 0
            j = 0

            while i < 5:  # Initiating loop for logging in
                username = input("\n\tUsername: ")
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

                            user_id = userpass_adm[username][1]
                            user_info_list = [username]

                            for i in userpass_adm[username]:
                                if i == user_id:
                                    continue
                                else:
                                    user_info_list.append(i)

                            user_info = {user_id: user_info_list}
                            check = 'Successful'
                            break

                        elif password != userpass_adm[username][0]:
                            print("\tInvalid username or password\n\tPlease enter again")
                            i += 1
                            continue

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
                            check = 'Unsuccessful'
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
                    print("\tInvalid option")
                    print("\tRe-enter your info. again")
                    continue

            # Breaking from loop if successfully passed the checking
            if check == 'Successful':
                if (username == user_info[user_id][0]) and (password == user_info[user_id][1]):
                    break

            elif check == 'Unsuccessful':
                continue

        # -----------------------------------------------------------------------------------------------------------------------

        elif user_inp_2 == '2':  # Login as student
            print("\n\n\n\t---------LOGIN(STUDENT)---------")

            # Assigning Userpass_Std Sheet to New var
            userpass_std_xl = pd.read_excel(userpass, 'Students')

            # Usernames : Password as key value pair
            user_infos = list(zip(userpass_std_xl.PASSWORDS, userpass_std_xl.USER_IDS,
                                  userpass_std_xl.NAME, userpass_std_xl.CLASS,
                                  userpass_std_xl.SEC, userpass_std_xl.EMAIL, userpass_std_xl.ROLE))
            userpass_std = dict(zip(userpass_std_xl.USERNAMES, user_infos))

            # Variable to control the no. of times user can keep entering wrong password
            i = 0
            j = 0

            while i < 5:  # Initiating loop for logging in
                username = input("\n\tUsername: ")
                password = input("\tPassword: ")
                user_inp_3 = input("\tConfirm to proceed (Y/N): ")

                if (user_inp_3.upper() == 'Y') or (user_inp_3.capitalize() == 'Yes'):

                    # Executes if proper credentials were entered.
                    time.sleep(2)
                    if username in userpass_std:
                        if password == userpass_std[username][0]:
                            print("\tThank you")
                            time.sleep(2)
                            print("\tYou will shortly be taken away from login page")

                            user_id = userpass_std[username][1]
                            user_info_list = [username]

                            for i in userpass_std[username]:
                                if i == user_id:
                                    continue
                                else:
                                    user_info_list.append(i)

                            user_info = {user_id: user_info_list}
                            check = 'Successful'
                            break

                        elif password != userpass_std[username][0]:
                            print("\tInvalid username or password\n\tPlease enter again")
                            i += 1
                            continue

                    elif username not in userpass_std:
                        if j < 2:
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
                            check = 'Unsuccessful'
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
                    print("\tInvalid option")
                    print("\tRe-enter your info. again")
                    continue

            # Breaking from loop if successfully passed the checking
            if check == 'Successful':
                if (username == user_info[user_id][0]) and (password == user_info[user_id][1]):
                    break

            elif check == 'Unsuccessful':
                continue
        # -----------------------------------------------------------------------------------------------------------------------

        elif user_inp_2 == '3':
            print("\tYou'll be taken back")
            break

        # Executes when invalid number has been entered
        else:
            print("\tEnter a Valid Number")
            continue


def signup():
    global username_adm, password_adm, ids_adm, name_adm, t_nt_adm, role_adm, post_adm, email_adm
    global username_std, password_std, ids_std, name_std, clss_std, sec_std, role_std, email_std
    global username, password
    while True:
        print("\n\n\n\t---------SIGNUP---------")
        print("\n\tSignup as:\n\t1. Admin\n\t2. Student\n\t3. Go Back")
        user_inp_2 = input("\tChoose (Enter number): ")

        # Signup as admin
        time.sleep(2)
        if user_inp_2 == '1':

            obtain_data_adm()

            print("\n\n\n\t---------SIGNUP(ADMIN)---------")

            # Taking Information related to user
            print("\n\t------RULES------")
            print("\tFor Username:-")
            print("\tUse any key other than '@'")
            print("\n\tFor Password:-")
            print("\tPassword must consist of the following:")
            print("\t1. 8-20 Characters long")
            print("\t2. Consist of letters A-Z and a-z")
            print("\t3. Consist of digits 0-9")
            print("\t4. Consist of any special characters")

            while True:
                username = input("\n\tUsername: ")

                if '@' in username:
                    print("\n\tInvalid Username")
                    print("\tConsists of @")
                    print("\tPlease enter again")
                    continue

                if username in username_adm:
                    print("\tUsername has already been taken")
                    print("\t1. Login")
                    print("\t2. Signin using another username")
                    user_inp_3 = input("\tChoose (Enter number only): ")

                    if user_inp_3 == '1':
                        print("\n\tYou'll be taken to the Login page")
                        input("\tPress Enter to continue")
                        check = 'Existing'
                        break
                    elif user_inp_3 == '2':
                        print("\n\tPlease use another username")
                        print("\tYou'll be taken to the Signin page")
                        check = 'Signin'
                        break
                    else:
                        print("\n\tInvalid option entered")
                        print("\tPlease enter again")
                        print("\tYou'll be taken back to username page")
                        continue

                else:
                    print("\n\tValid Username")
                    check = 'Successful'
                    break

            if check == 'Existing':
                break
            elif check == 'Signin':
                continue

            # Loop to ensure Valid password is entered
            while True:
                password = input("\tPassword: ")
                password_check()

                if check == 'Successful':
                    break

                else:
                    continue

            # Taking Inputs as first name and last name and individually holding checks
            while True:
                time.sleep(2)
                print("\n\n\n\t---------PERSONAL INFORMATION---------")
                f_name = input("\n\tFirst Name: ")
                l_name = input("\tLast Name: ")

                # Ensuring user has entered or typed their names correctly
                time.sleep(1)
                print("\n\t1. Proceed (No error)\n\t2. Repeat (Error)")
                user_inp_4 = input("\tChoose (Enter number): ")

                # Executes if user has no errors in their name
                time.sleep(2)
                if user_inp_4 == '1':

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
                elif user_inp_4 == '2':
                    continue

                else:
                    print("\tInvalid number entered")
                    print("\tPLease renter your personal information")
                    continue

            time.sleep(2)
            print("\n\t1. Teaching\n\t2. Non-Teaching")
            user_inp_5 = input("\tChoose (Enter number): ")

            time.sleep(1)
            if user_inp_5 == '1':
                t_nt = 'Teaching'
                role = 'Admin'
                post = input("\tPost: ")

            elif user_inp_5 == '2':
                t_nt = 'Non_Teaching'
                role = 'Admin'
                post = input("\tPost: ")

            elif user_inp_5 != '1' or user_inp_5 != '2':
                print("\tEnter your info again")
                continue

            # Taking Email as input
            while True:
                time.sleep(1)
                print("\n\tCurrently accepting only emails with the following domains:")
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

            assign_userid_adm()

            # Appending new values entered to lists
            username_adm.append(username)
            password_adm.append(password)
            ids_adm.append(user_id)
            name_adm.append(name)
            t_nt_adm.append(t_nt)
            role_adm.append(role)
            post_adm.append(post)
            email_adm.append(email)

            transfer_data_adm()

            time.sleep(1)
            print("\n\tThank you for signing up")
            time.sleep(2)
            print("\n\tYou will be taken to the login page")
            time.sleep(2)
            break

        # -----------------------------------------------------------------------------------------------------------------------

        # Signup as Student
        elif user_inp_2 == '2':

            print("\n\n\n\t---------SIGNUP(STUDENT)---------")

            obtain_data_std()

            # Taking Information related to user
            print("\n\t------RULES------")
            print("\tFor Username:-")
            print("\tUse any key other than '@'")
            print("\n\tFor Password:-")
            print("\tPassword must consist of the following:")
            print("\t1. 8-20 Characters long")
            print("\t2. Consist of letters A-Z and a-z")
            print("\t3. Consist of digits 0-9")
            print("\t4. Consist of any special characters")

            while True:
                username = input("\n\tUsername: ")

                if '@' in username:
                    print("\n\tInvalid Username")
                    print("\tConsists of @")
                    print("\tPlease enter again")
                    continue

                if username in username_std:
                    print("\tUsername has already been taken")
                    print("\t1. Login")
                    print("\t2. Signin using another username")
                    user_inp_3 = input("\tChoose (Enter number only): ")

                    if user_inp_3 == '1':
                        print("\n\tYou'll be taken to the Login page")
                        input("\tPress Enter to continue")
                        check = 'Existing'
                        break
                    elif user_inp_3 == '2':
                        print("\n\tPlease use another username")
                        print("\tYou'll be taken to the Signin page")
                        check = 'Signin'
                        break
                    else:
                        print("\n\tInvalid option entered")
                        print("\tPlease enter again")
                        print("\tYou'll be taken back to username page")
                        continue

                else:
                    print("\n\tValid Username")
                    break

            if check == 'Existing':
                break
            elif check == 'Signin':
                continue

            # Loop to ensure Valid password is entered
            while True:
                password = input("\tPassword: ")
                password_check()

                if check == 'Successful':
                    break

                else:
                    continue

            # Taking Inputs as first name and last name and individually holding checks
            while True:
                time.sleep(2)
                print("\n\n\n---------PERSONAL INFORMATION---------")
                f_name = input("\n\tFirst Name: ")
                l_name = input("\tLast Name: ")

                # Ensuring user has entered or typed their names correctly
                time.sleep(1)
                print("\n\t1. Proceed (No error)\n\t2. Repeat (Error)")
                user_inp_4 = input("\tChoose (Enter number): ")

                # Executes if user has no errors in their name
                time.sleep(2)
                if user_inp_4 == '1':

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
                elif user_inp_4 == '2':
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
                    '''
                    print("\tA 6-Code OTP has been sent to your e-mail")
                    otp = int(input("Enter the OTP: "))
                    if otp sent == otp entered:
                        print("\tValid OTP entered")
                    else:
                        print("\tInvalid OTP Entered)
                        continue
                    '''
                    print("\tValid E-mail")
                    break
                else:
                    print("\tInvalid Email")
                    continue

            assign_userid_std()

            # Appending new values entered to the lists
            username_std.append(username)
            password_std.append(password)
            ids_std.append(user_id)
            name_std.append(name)
            clss_std.append(clss)
            sec_std.append(sec)
            role_std.append(role)
            email_std.append(email)

            transfer_data_std()

            time.sleep(1)
            print("\n\tThank you for signing up")
            time.sleep(2)
            print("\n\tYou will be taken to the login page")
            time.sleep(2)
            break

        # -----------------------------------------------------------------------------------------------------------------------

        elif user_inp_2 == '3':
            print("\tYou'll be taken back")
            break

        else:
            print("\tEnter a Valid Number")
            continue


def assign_userid_adm():
    global user_id
    # List containing all the numbers used for ids
    ids_used = []

    for i in ids_adm:
        split = i.partition('@')
        id_num_used = int(split[2])
        ids_used.append(id_num_used)

    # Loop for Assigning numbers; hence creating a user id
    while True:
        i = r.randrange(100, 121)
        if i not in ids_used:
            user_id = username + '@' + str(i)
            break


def assign_userid_std():
    global user_id
    ids_used = []
    # Loop for partitioning ids into numbers and appending numbers to ids_used
    for i in ids_std:
        split = i.partition('@')
        id_num_used = int(split[2])
        ids_used.append(id_num_used)

    # Loop for Assigning numbers; hence creating a user id
    while True:
        i = r.randint(100, 120)
        if i not in ids_used:
            user_id = username + '@' + str(i)
            break


def edit_username():
    global check
    while True:
        print("\n\n\n\t---------EDIT USERNAME---------")

        if role == 'Admin':
            while True:
                obtain_data_adm()
                username = input("\n\tCurrent Username: ")

                if username in username_adm:
                    user_inp_7 = input("\n\tDo you really want to change your username? (Yes/No): ")

                    if user_inp_7.lower() == 'yes':
                        while True:
                            print("\n\t------RULES------")
                            print("\tUse any key other than '@'")
                            new_username = input("\n\tNew Username: ")
                            confirm_username = input("\tConfirm Username: ")

                            if '@' in new_username:
                                print("\n\tInvalid Username")
                                print("\tConsists of @")
                                print("\tPlease enter again")
                                continue

                            if new_username == confirm_username:
                                for i in range(0, len(username_adm)):
                                    if username_adm[i] == username:
                                        index_username = i
                                        username_adm.remove(username)
                                        break

                                for i in range(0, len(ids_adm)):
                                    if ids_adm[i] == user_id:
                                        index_userid = i
                                        ids_adm.remove(username)
                                        break

                                assign_userid_adm()

                                username_adm.insert(index_username, new_username)
                                ids_adm.insert(index_userid, user_id)
                                print("\n\tYour username has been updated")
                                print("\tYou'll be taken to the login page")
                                break

                            else:
                                print("\n\tUsernames don't match with each other")
                                print("\tPlease enter again")
                                continue

                    elif user_inp_7.lower() == 'no':
                        print("\n\tYou'll be taken back to Edit Account information")
                        check = 'Break'
                        break

                    else:
                        print("\n\tInvalid option entered")
                        print("\tEnter option again")
                        continue

                elif username not in username_adm:
                    print("\n\tInvalid username entered")
                    print("\tPlease enter again")
                    continue

                if (new_username in username_adm) and (user_id in ids_adm):
                    transfer_data_adm()
                    check = 'Successful'
                    break

        elif role == 'Student':
            while True:
                obtain_data_std()
                username = input("\n\tCurrent Username: ")

                if username in username_std:
                    user_inp_7 = input("\n\tDo you really want to change your username? (Yes/No): ")

                    if user_inp_7.lower() == 'yes':
                        while True:
                            print("\n\t------RULES------")
                            print("\tUse any key other than '@'")
                            new_username = input("\n\tNew Username: ")
                            confirm_username = input("\tConfirm Username: ")

                            if new_username == confirm_username:
                                for i in range(0, len(username_std)):
                                    if username_std[i] == username:
                                        index_username = i
                                        username_std.remove(username)
                                        break

                                for i in range(0, len(ids_std)):
                                    if ids_std[i] == user_id:
                                        index_userid = i
                                        ids_std.remove(user_id)

                                assign_userid_std()

                                username_std.insert(index_username, new_username)
                                ids_std.insert(index_userid, user_id)
                                print("\n\tYour username has been updated")
                                print("\tYou'll be taken to the login page")
                                break

                            else:
                                print("\n\tUsernames don't match with each other")
                                print("\tPlease enter again")
                                continue

                    elif user_inp_7.lower() == 'no':
                        print("\n\tYou'll be taken back to Edit Account information")
                        check = 'Break'
                        break

                    else:
                        print("\n\tInvalid option entered")
                        print("\tEnter option again")

                elif username not in username_std:
                    print("\n\tInvalid username entered")
                    print("\tPlease enter again")
                    continue

                if new_username in username_std:
                    transfer_data_std()
                    check = 'Successful'
                    break

        if (check == 'Successful') or (check == 'Break'):
            break


def edit_password():
    while True:
        print("\n\n\n\t---------EDIT PASSWORD---------")

        # List of special characters to ensure password consists of them
        spec_ch = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',
                   '[', ']', '{', '}', ';', ':', '<', '>', '/', '\\', '|', ' ']

        if role == 'Admin':
            while True:
                obtain_data_adm()
                org_password = input("\n\tCurrent Password: ")

                if org_password in password_adm:
                    user_inp_7 = input("\n\tDo you really want to change your org_password? (Yes/No): ")

                    if user_inp_7.lower() == 'yes':
                        while True:
                            print("\n\n\n---------NEW PASSWORD---------")
                            print("\n\t------RULES------")
                            print("\tPassword must consist of the following:")
                            print("\t1. 8-20 Characters long")
                            print("\t2. Consist of letters A-Z and a-z")
                            print("\t3. Consist of digits 0-9")
                            print("\t4. Consist of any special characters")
                            password = input("\n\tNew Password: ")
                            confirm_password = input("\tConfirm Password: ")
                            password_check()

                            if password == confirm_password:
                                for i in range(0, len(password_adm)):
                                    if password_adm[i] == org_password:
                                        index = i
                                        password_adm.remove(org_password)
                                        break
                                password_adm.insert(index, password)
                                print("\n\tYour password has been updated")
                                print("\tYou'll be taken to the login page")
                                break

                            else:
                                print("\n\tPasswords don't match with each other")
                                print("\tPlease enter again")
                                continue

                    elif user_inp_7.lower() == 'no':
                        print("\n\tYou'll be taken back to Edit Account information")
                        check = 'Break'
                        break

                    else:
                        print("\n\tInvalid option entered")
                        print("\tEnter option again")
                        continue

                elif org_password not in password_adm:
                    print("\n\tInvalid password entered")
                    print("\tPlease enter again")
                    continue

                if password in password_adm:
                    transfer_data_adm()
                    check = 'Successful'
                    break

        elif role == 'Student':
            while True:
                obtain_data_std()
                org_password = input("\n\tCurrent Password: ")

                if org_password in password_std:
                    user_inp_7 = input("\n\tDo you really want to change your org_password? (Yes/No): ")

                    if user_inp_7.lower() == 'yes':
                        while True:
                            print("\n\n\n---------NEW PASSWORD---------")
                            print("\n\t------RULES------")
                            print("\tPassword must consist of the following:")
                            print("\t1. 8-20 Characters long")
                            print("\t2. Consist of letters A-Z and a-z")
                            print("\t3. Consist of digits 0-9")
                            print("\t4. Consist of any special characters")
                            password = input("\n\tNew Password: ")
                            confirm_password = input("\tConfirm Password: ")
                            password_check()

                            if password == confirm_password:
                                for i in range(0, len(password_std)):
                                    if password_std[i] == org_password:
                                        index = i
                                        password_std.remove(org_password)
                                        break
                                password_std.insert(index, password)
                                print("\n\tYour password has been updated")
                                print("\tYou'll be taken to the login page")
                                break

                            else:
                                print("\n\tPasswords don't match with each other")
                                print("\tPlease enter again")
                                continue

                    elif user_inp_7.lower() == 'no':
                        print("\n\tYou'll be taken back to Edit Account information")
                        check = 'Break'
                        break

                    else:
                        print("\n\tInvalid option entered")
                        print("\tEnter option again")

                elif org_password not in password_std:
                    print("\n\tInvalid password entered")
                    print("\tPlease enter again")
                    continue

                if password in password_std:
                    transfer_data_std()
                    check = 'Successful'
                    break

        if (check == 'Successful') or (check == 'Break'):
            break


def edit_email():
    while True:
        print("\n\n\n\t---------EDIT EMAIL---------")

        if role == 'Admin':
            while True:
                obtain_data_adm()
                email = input("\n\tCurrent Email: ")

                if email in email_adm:
                    user_inp_7 = input("\n\tDo you really want to change your email? (Yes/No): ")

                    if user_inp_7.lower() == 'yes':
                        while True:
                            print("\n\tCurrently accepting only emails with the following domains:")
                            print("\t1. @gmail.com")
                            print("\t2. @hotmail.com")
                            print("\t3. @yahoo.com")
                            new_email = input("\n\tNew Email: ")
                            confirm_email = input("\tConfirm Email: ")

                            if (new_email.endswith("@gmail.com") or
                                    new_email.endswith("@hotmail.com") or
                                    new_email.endswith("@yahoo.com")):
                                print("\n\tValid E-mail")
                            else:
                                print("\n\tInvalid Email")
                                continue

                            if new_email == confirm_email:
                                for i in range(0, len(email_adm)):
                                    if email_adm[i] == email:
                                        index = i
                                        email_adm.remove(email)
                                        break
                                email_adm.insert(index, new_email)
                                print("\n\tYour email has been updated")
                                print("\tYou'll be taken to the login page")
                                break

                            else:
                                print("\n\tEmails don't match with each other")
                                print("\tPlease enter again")
                                continue

                    elif user_inp_7.lower() == 'no':
                        print("\n\tYou'll be taken back to Edit Account information")
                        check = 'Break'
                        break

                    else:
                        print("\n\tInvalid option entered")
                        print("\tEnter option again")
                        continue

                elif email not in email_adm:
                    print("\n\tInvalid email entered")
                    print("\tPlease enter again")
                    continue

                if new_email in email_adm:
                    transfer_data_adm()
                    check = 'Successful'
                    break

        elif role == 'Student':
            while True:
                obtain_data_std()
                email = input("\n\tCurrent Email: ")

                if email in email_std:
                    user_inp_7 = input("\n\tDo you really want to change your email? (Yes/No): ")

                    if user_inp_7.lower() == 'yes':
                        while True:
                            print("\n\tCurrently accepting only emails with the following domains:")
                            print("\t1. @gmail.com")
                            print("\t2. @hotmail.com")
                            print("\t3. @yahoo.com")
                            new_email = input("\n\tNew Email: ")
                            confirm_email = input("\tConfirm Email: ")

                            if (new_email.endswith("@gmail.com") or
                                    new_email.endswith("@hotmail.com") or
                                    new_email.endswith("@yahoo.com")):
                                print("\n\tValid E-mail")
                            else:
                                print("\n\tInvalid Email")
                                continue

                            if new_email == confirm_email:
                                for i in range(0, len(email_std)):
                                    if email_std[i] == email:
                                        index = i
                                        email_std.remove(email)
                                        break
                                email_std.insert(index, new_email)
                                print("\n\tYour Email has been updated")
                                print("\tYou'll be taken to the login page")
                                break

                            else:
                                print("\n\tEmails don't match with each other")
                                print("\tPlease enter again")
                                continue

                    elif user_inp_7.lower() == 'no':
                        print("\n\tYou'll be taken back to Edit Account information")
                        check = 'Break'
                        break

                    else:
                        print("\n\tInvalid option entered")
                        print("\tEnter option again")

                elif email not in email_std:
                    print("\n\tInvalid email entered")
                    print("\tPlease enter again")
                    continue

                if new_email in email_std:
                    transfer_data_std()
                    check = 'Successful'
                    break

        if (check == 'Successful') or (check == 'Break'):
            break


def edit_acc_info():
    while True:
        print("\n\n\n\t---------EDIT ACCOUNT INFORMATION---------")
        print("\n\t1. Edit Username")
        print("\t2. Edit Password")
        print("\t3. Go Back")
        user_inp_6 = input("\tChoose (Enter number only): ")

        if user_inp_6 == '1':
            # Edit Username
            edit_username()
            if check == 'Break':
                break
            elif check == 'Successful':
                if role == 'Admin':
                    obtain_data_adm()
                elif role == 'Student':
                    obtain_data_std()
                login()
                assign_values()
                break

        elif user_inp_6 == '2':
            # Edit Password
            edit_password()
            if role == 'Admin':
                obtain_data_adm()
            elif role == 'Student':
                obtain_data_std()
            login()
            assign_values()
            break

        elif user_inp_6 == '3':
            break

        else:
            print("\tInvalid Number")
            print("\tPlease Enter a Valid Option after taken back")
            continue


def acc_info():
    while True:
        print("\n\n\n\t---------ACCOUNT INFORMATION---------")
        print(f"\n\tUser ID: {user_id}")
        print(f"\tUsername: {username}")
        print(f"\tRole: {role}")
        print("\t1. Edit Account Information")
        print("\t2. Go Back")
        user_inp_5 = input("\tChoose (Enter number only): ")

        if user_inp_5 == '1':
            edit_acc_info()

        elif user_inp_5 == '2':
            print("\tYou'll be taken to the Profile Page")
            break

        else:
            print("\tInvalid Number")
            print("\tPlease Enter a Valid Option after taken back")


def edit_per_info():
    while True:
        print("\n\n\n\t---------EDIT PERSONAL INFORMATION---------")
        print("\t1. Edit Email")

        if role == 'Admin':
            print("\t2. Edit Post")
            print("\t3. Go Back")

        elif role == 'Student':
            print("\t2. Edit Class")
            print("\t3. Edit Section")
            print("\t4. Go Back")

        user_inp_6 = input("\tChoose (Enter number only): ")

        if user_inp_6 == '1':
            edit_email()
            if role == 'Admin':
                obtain_data_adm()
            elif role == 'Student':
                obtain_data_std()
            login()
            assign_values()
            break

        elif user_inp_6 == '2':
            if role == 'Admin':
                print("\n\n\n\t---------EDIT POST---------")
                pass

            elif role == 'Student':
                print("\n\n\n\t---------EDIT CLASS---------")
                pass

        elif user_inp_6 == '3':
            if role == 'Admin':
                break

            elif role == 'Student':
                print("\n\n\n\t---------EDIT SECTION---------")
                pass

        elif user_inp_6 == '4':
            if role == 'Admin':
                print("\tInvalid Number")
                print("\tPlease Enter a Valid Option after taken back")
                continue

            elif role == 'Student':
                break

        else:
            print("\tInvalid Number")
            print("\tPlease Enter a Valid Option after taken back")
            continue


def per_info():
    while True:
        print("\n\n\n\t---------PERSONAL INFORMATION---------")
        print(f"\n\tName: {name}")

        if role == 'Admin':
            print(f"\tTeaching/Non-Teaching: {t_nt}")
            print(f"\tPost: {post}")

        if role == 'Student':
            print(f"\tClass: {clss}")
            print(f"\tSection: {sec}")

        print(f"\tEmail: {email}")
        print("\n\t1. Edit Personal Information")
        print("\t2. Go Back")
        user_inp_5 = input("\tChoose (Enter number only): ")

        if user_inp_5 == '1':
            edit_per_info()

        elif user_inp_5 == '2':
            print("\tYou'll be taken to the Profile Page")
            break

        else:
            print("\tInvalid Number")
            print("\tPlease Enter a Valid Option after taken back")
            continue


def profile():
    # Profile Function for Admin & Student
    while True:
        print("\n\n\n\t---------PROFILE---------")
        print("\n\t1. View Account Information")
        print("\t2. View Personal Information")
        print("\t3. Go Back")
        user_inp_4 = input("\tChoose (Enter number only): ")

        # Profile Options for Admin
        if user_inp_4 == '1':
            acc_info()

        elif user_inp_4 == '2':
            if role == 'Admin':
                per_info()

            elif role == 'Student':
                per_info()

        elif user_inp_4 == '3':
            print("\tYou'll be taken to the Settings Page")
            break

        else:
            print("\tInvalid Number")
            print("\tPlease Enter a Valid Option after taken back")
            continue


def logout():
    global check
    print("\n\n\n\t---------LOGOUT---------")
    user_inp_4 = input("\tDo you really wanna logout? (Yes/No): ")
    if user_inp_4.lower() == 'yes':
        print("\tThank You")
        print("\tYou'll be taken to the Login/Signup Page")
        check = 'Break'

    elif user_inp_4.lower() == 'no':
        print("\tThank you")
        print("\tYou'll be taken to Settings page")


def settings_adm():
    while True:
        print("\n\n\n\t---------SETTINGS---------")
        print("\n\t1. Profile")
        print("\t2. Log out")
        print("\t3. Go Back")
        user_inp_3 = input("\tChoose (Enter number only): ")

        # Displays Profile of User
        if user_inp_3 == '1':
            profile()

        # Displays Logout
        elif user_inp_3 == '2':
            logout()
            if check == 'Break':
                break
            else:
                continue

        elif user_inp_3 == '3':
            break

        else:
            print("\tEnter a valid option after being taken back")
            continue


def settings_std():
    global check
    while True:
        print("\n\n\n\t---------SETTINGS---------")
        print("\n\t1. Profile")
        print("\t2. Participation status")
        print("\t3. Log out")
        print("\t4. Go Back")
        user_inp_3 = input("\tChoose (Enter number only): ")

        # Display Profile of the user
        if user_inp_3 == '1':
            profile()

        # Display Participation Status of user
        elif user_inp_3 == '2':
            while True:
                print("\n\n\n\t---------PARTICIPATION STATUS---------")
                print("\tAll participation status will be printed alongside the events")
                print("\tDisplay list of events Participating/participated in")
                print("\t1. Ongoing\n\t2. Completed")
                break

        # Display Logout
        elif user_inp_3 == '3':
            logout()

            if check == 'Break':
                break
            else:
                continue

        elif user_inp_3 == '4':
            check = 'Continue'
            break


# Actual Program
while True:
    print("\t---------EVENT MANAGEMENT SYSTEM---------")
    print("\n\n\n\t---------WELCOME---------")
    print("\t1. Login/Signup")
    print("\t2. Exit Application")
    user_inp_main = input("\tChoose (Enter number only): ")
    time.sleep(2)

    # Displaying Login/Signup Interface
    if user_inp_main == '1':
        while True:
            print("\n\n\n\t---------LOGIN/SIGNUP---------")
            print("\t1. Login\n\t2. Signup\n\t3. Go Back")
            user_inp_1 = input("\tChoose (Enter number): ")

            # Assigning path of file to a variable
            root = r"C:\Users\97150\PycharmProjects\Event_Mng_Sys\Account_Signin.xlsx"

            # Obtaining Excel file containing Usernames and passwords
            userpass = pd.ExcelFile(root)

            if user_inp_1 == '1':
                login()
                break

            elif user_inp_1 == '2':
                signup()

            elif user_inp_1 == '3':
                print("You'll be taken back")
                break

            else:
                print("\tEnter a Valid Option: ")
                continue

    elif user_inp_main == '2':
        print("\tThank you for opening our application")
        print("\tThe app will be closed shortly")
        time.sleep(5)
        break

    else:
        print("\tEnter a valid option after being taken back")
        continue

    if check == 'Successful':
        assign_values()

    else:
        break
    # Displaying Interface
    # Admin Interface
    if role == 'Admin':
        while True:
            print("\n\n\n\t---------HOME---------")
            print("\n\t1. Events")
            print("\t2. Post")
            print("\t3. Settings")
            user_inp_2 = input("\tChoose (Enter number only): ")

            # Displays Events
            if user_inp_2 == '1':
                while True:
                    print("\n\n\n\t---------EVENTS---------")
                    print("\tAll details regarding ongoing events will be printed")
                    break

            # Displays Post
            elif user_inp_2 == '2':
                while True:
                    print("\n\n\n\t---------POST---------")
                    print("\n\t1. Announcements")
                    print("\t2. Participation List")
                    print("\t3. Winners")
                    print("\t4. Exit")
                    user_inp_3 = input("\tChoose (Enter number only): ")

                    # Displays Announcements
                    if user_inp_3 == '1':
                        while True:
                            print("\n\n\n\t------------ANNOUNCEMENTS---------")
                            print("\n\tAnnounce the following")
                            print("\t1. New Event")
                            print("\t2. New Notice")
                            print("\t3. Edit Event")
                            print("\t4. Edit Notice")
                            print("\t5. Exit")
                            user_inp_4 = input("\tChoose (Enter number only): ")

                            # Displays Event Announcement
                            if user_inp_4 == '1':
                                print("\n\n\n\t---------EVENT ANNOUNCEMENT---------")
                                print("\tDisplay the post button of an event")
                                print("\tAllow them to deploy circulars")

                            # Displays Notice Announcement
                            elif user_inp_4 == '2':
                                print("\n\n\n---------NOTICE ANNOUNCEMENT---------")
                                print("\tDisplay the post button of a notice")

                            # Displays Edit Event
                            elif user_inp_4 == '3':
                                print("\n\n\n\t---------EDIT EVENT---------")
                                print("\tDisplay all the events and let the user choose which one to edit")

                            # Displays Edit Notice
                            elif user_inp_4 == '4':
                                print("\n\n\n\t---------EDIT NOTICE---------")
                                print("\tDisplay all the notices and let the user choose which one to edit")

                            elif user_inp_4 == '5':
                                break

                    # Displays Ongoing events and their Participation
                    elif user_inp_3 == '2':
                        while True:
                            print("\n\n\n\t---------PARTICIPATION---------")
                            print("\tDisplay all the Events Titles")
                            print("\tAllow the user to choose the participation list from that event")
                            break

                    # Displays Winner Option to announce winner
                    elif user_inp_3 == '3':
                        while True:
                            print("\n\n\n\t---------WINNERS---------")
                            print("\tLet user choose an event")
                            print("\tLet user announce the winners names and so on")
                            break

                    elif user_inp_4 == '4':
                        break

            # Displays Settings
            elif user_inp_2 == '3':
                settings_adm()

                if check == 'Break':
                    break
                elif check == 'Continue':
                    continue

    # Student Interface
    elif role == 'Student':
        while True:
            print("\n\n\n\t---------HOME---------")
            print("\n\t1. Events")
            print("\t2. Post")
            print("\t3. Settings")
            user_inp_2 = input("\tChoose (Enter number only): ")

            # Display Events
            if user_inp_2 == '1':
                while True:
                    print("\n\n\n\t---------EVENTS---------")
                    print("\tAll details regarding ongoing events will be printed")
                    break

            # Display Post
            elif user_inp_2 == '2':
                while True:
                    print("\n\n\n\t---------POST---------")
                    print("\n\t1. Event Participation")
                    print("\t2. Circular/Form Fill")
                    user_inp_3 = input("\tChoose (Enter number only): ")

                    # Display Event Participation
                    if user_inp_3 == '1':
                        while True:
                            print("\n\n\n\t---------EVENT PARTICIPATION---------")
                            print("\tDisplay all the ongoing events")
                            print("\t(Possible events to participate in)")
                            break

                    # Display Circulars/Forms to be filled
                    elif user_inp_3 == '2':
                        while True:
                            print("\n\n\n\t---------CIRCULAR/FORM FILL---------")
                            print("\tDisplay all the circulars related to ongoing events")
                            break

            # Display Settings
            elif user_inp_2 == '3':
                settings_std()

                if check == 'Break':
                    break
                elif check == 'Continue':
                    continue
