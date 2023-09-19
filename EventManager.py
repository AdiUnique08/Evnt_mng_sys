import csv
import time
import random as r
import sys
from tabulate import tabulate
import copy

#Reference of files title
"""
l1 = ['SNO', 'USERNAME', 'PASSWORD', 'NAME', 'CLASS', 'SECTION', 'EMAIL', 'USERID', 'ROLE']
l2 = ['SNO', 'USERNAME', 'PASSWORD', 'NAME', 'SUBJECT', 'LEVEL', 'EMAIL', 'USERID', 'ROLE']
l3 = ['SNO', 'USERNAME', 'PASSWORD', 'NAME', 'TYPE', 'STAFF_ROLE', 'EMAIL', 'USERID', 'ROLE']
"""


def login(root, role):
    if role == '1':
        print("\n\n\n\t\t------LOGIN(STUDENT)------\n")
    elif role == '2':
        print("\n\n\n\t\t------LOGIN(TEACHER)------\n")
    elif role == '3':
        print("\n\n\n\t\t------LOGIN(NON-TEACHER)------\n")
    c = 0
    while True:
        for i in range(5):
            with open(root, 'r') as f:
                flag = False
                read = csv.reader(f)
                username = input("\tUsername: ")
                for j in read:
                    if username == j[1]:
                        flag = True
                        print("\tUser Authorized\n")
                        break
                if flag == False:
                    print("\tUsername not found")
                    print("\tPlease reenter again\n")
                elif flag == True:
                    break
        if flag == False:
            cancel = input("\tDo you want to cancel the Login process? (Y/N): ")
            if cancel.lower() == 'y':
                print("\tLogin process is cancelled")
                print("\tYou'll be taken back")
                return "Fail", []
            print("\tPlease wait for 15 seconds\n")
            c += 1
            if c == 3:
                print("\tYou are forcibly exited\n\n\n")
                return "Fail", []
            time.sleep(15)
        elif flag == True:
            break

    if flag == True:
        c = 0
        while True:
            for i in range(5):
                with open(root, 'r') as f:
                    flag = False
                    read = csv.reader(f)
                    password = input("\tPassword: ")
                    for j in read:
                        if password == j[2]:
                            print("\tUser Authenticated")
                            return "Success", j
                if flag == False:
                    print("\tPassword not found")
                    print("\tPlease reenter again\n")

            if flag == False:
                cancel = input("\tDo you want to cancel the Login process? (Y/N): ")
                if cancel.lower() == 'y':
                    print("\tLogin process is cancelled")
                    print("\tYou'll be taken back")
                    return "Fail", []
                print("\tPlease wait for 15 seconds\n")
                c += 1
                if c == 3:
                    print("\tYou are forcibly exited\n\n\n")
                    return "Fail", []
                time.sleep(15)


def generate(root, name):
    l_userids = []
    with open(root) as f:
        read = csv.reader(f)
        x = -1
        for i in read:
            x += 1
            if x == 0:
                continue
            else:
                l_userids.append(i[7])
    num_used = []
    for i in l_userids:
        temp = i.partition('@')
        num_used.append(temp[2])
    while True:
        rand_num = r.randrange(100, 500)
        if str(rand_num) in num_used:
            continue
        else:
            break
    ID = name.replace(" ", '_') + '@' + str(rand_num)
    return ID


def signup(root, role):
    info = []
    if role == '1':
        print("\n\n\n\t\t------SIGNUP(STUDENT)------\n")
        role = 'Student'
    elif role == '2':
        print("\n\n\n\t\t------SIGNUP(TEACHER)------\n")
        role = 'Teacher'
    elif role == '3':
        print("\n\n\n\t\t------SIGNUP(NON-TEACHER)------\n")
        role = 'Non-Teacher'
    while True:
        print("\n\t\t\t------RULES------")
        print("\tFor Username:-")
        print("\tUse any key other than '@'\n")
        flag = False
        username = input("\tUsername: ")
        edit = input("\tDo you want to edit it? (Y/N): ")
        if edit.lower() == 'y':
            print("\tYou're allowed to edit it")
            continue
        if '@' in username:
            print(f"\tInvalid key '@' found")
            print("\tPlease reenter your username")
            flag = True
        if flag == False:
            with open(root, 'r') as f:
                read = csv.reader(f)
                x = -1
                for i in read:
                    x += 1
                    if username == i[1]:
                        print("\tUsername already exists")
                        cancel = input("\tDo you want to login? (Y/N): ")
                        if cancel.lower() == 'y':
                            print("\tSignup process is cancelled")
                            print("\tYou'll be taken back")
                            return 'Fail', []
                        elif cancel.lower() == 'n':
                            flag = True
                            break
        if flag == True:
            cancel = input("\tDo you want to cancel the signup process? (Y/N): ")
            if cancel.lower() == 'y':
                print("\tSignup process is cancelled")
                print("\tYou'll be taken back")
                return 'Fail', []
            else:
                print("\tPlease reenter the username\n")

        cancel = input("\tDo you want to cancel the signup process? (Y/N): ")
        if cancel.lower() == 'y':
            print("\tSignup process is cancelled")
            print("\tYou'll be taken back")
            return 'Fail', []

        elif flag == False:
            print("\tValid Username")
            print("\tYou'll be taken further")
            info.append(x + 1)
            info.append(username)
            break

    while True:
        print("\n\n\t\t\t------RULES------")
        print("\tPassword must consist of the following:")
        print("\t1. 8-20 Characters long")
        print("\t2. Consist of letters A-Z and a-z")
        print("\t3. Consist of digits 0-9")
        print("\t4. Consist of any special characters")
        spec_ch = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',
                   '[', ']', '{', '}', ';', ':', '<', '>', '/', '\\', '|', ' ', '.', ',',
                   '?', '|']
        flag = True
        cl, cu, cd, cspec = 0, 0, 0, 0
        password = input("\tPassword: ")
        if len(password) >= 8 and len(password) <= 20:
            if password.isalnum() is False:
                for i in password:
                    if i >= 'a' and i <= 'z':
                        cl += 1
                    elif i >= 'A' and i <= 'Z':
                        cu += 1
                    elif i >= '0' and i <= '9':
                        cd += 1
                    elif i in spec_ch:
                        cspec += 1
                if cl>0 and cu>0 and cd>0 and cspec>0:
                    flag = True
                else:
                    flag = False
            else:
                print("\tEntered password doesn't contain any special characters")
                flag = False
        else:
            print("\tEntered password is either too long or too short")
            flag = False

        if flag == False:
            cancel = input("\tDo you want to cancel the signup process? (Y/N): ")
            if cancel.lower() == 'y':
                print("\tSignup process is cancelled")
                print("\tYou'll be taken back")
                return 'Fail', []
            else:
                print("\tPlease renter the password\n")
        else:
            check = False
            while True:
                confirm_pwd = input("\tConfirmation Password (Reenter the original password): ")
                edit = input("\tDo you want to edit it? (Y/N): ")
                if edit.lower() == 'y':
                    print("\tYou're allowed to edit it")
                    continue
                cancel = input("\tDo you want to cancel the signup process? (Y/N): ")
                if cancel.lower() == 'y':
                    print("\tSignup process is cancelled")
                    print("\tYou'll be taken back")
                    return 'Fail', []
                else:
                    if confirm_pwd == password:
                        print("\tValid Password")
                        print("\tYou'll be taken further")
                        check = True
                        break
                    else:
                        print("\tConfirmation password doesn't match with Actual Password")
                        print("\tPlease reenter your confirmation password")
            if check == True:
                break
    info.append(password)

    while True:
        print("\n\n\t\t---PERSONAL INFORMATION---")
        print("\n\n\t\t\t------NOTE------")
        print("\t1. You will currently be entering your personal information")
        print("\t2. Please be aware while typing")
        print("\t3. You will be given a chance to edit")
        print("\t4. You will be a given chance to cancel the Signup process at each step")

        while True:
            name = input("\n\tName: ")
            edit = input("\tDo you want to edit it? (Y/N): ")
            cancel = input("\tDo you want to cancel the signup process? (Y/N): ")
            if edit.lower() == 'y':
                print("\tYou'll be allowed to edit")
            else:
                if cancel.lower() == 'y':
                    print("\tSignup process is cancelled")
                    print("\tYou'll be taken back")
                    return "Fail", []
                else:
                    print("\tYou'll be taken further")
                    break

        if role == 'Student':
            while True:
                clss = input("\n\tClass (Numbers only): ")
                edit = input("\tDo you want to edit it? (Y/N): ")
                cancel = input("\tDo you want to cancel the signup process? (Y/N): ")
                if edit.lower() == 'y':
                    print("\tYou'll be allowed to edit")
                else:
                    if cancel.lower() == 'y':
                        print("\tSignup process is cancelled")
                        print("\tYou'll be taken back")
                        return "Fail", []
                    else:
                        if (clss.isdigit() is True) and (len(clss) >= 1) and (len(clss) <=2):
                            print("\tYou'll be taken further")
                            break
                        else:
                            print("\tEntered class is invalid")
                            print("\tPlease reenter the class")

            while True:
                sec = input("\n\tSection (Capital letters only): ")
                edit = input("\tDo you want to edit it? (Y/N): ")
                cancel = input("\tDo you want to cancel the signup process? (Y/N): ")
                if edit.lower() == 'y':
                    print("\tYou'll be allowed to edit")
                else:
                    if cancel.lower() == 'y':
                        print("\tSignup process is cancelled")
                        print("\tYou'll be taken back")
                        return "Fail", []
                    else:
                        if (sec.isalpha() is True) and (sec.isupper() is True):
                            print("\tYou'll be taken further")
                            break
                        else:
                            print("\tEntered section is Invalid")
                            print("\tPlease reenter again")

        elif role == 'Teacher':
            while True:
                sub = input("\n\tSubject: ")
                edit = input("\tDo you want to edit it? (Y/N): ")
                cancel = input("\tDo you want to cancel the signup process? (Y/N): ")
                if edit.lower() == 'y':
                    print("\tYou'll be allowed to edit")
                else:
                    if cancel.lower() == 'y':
                        print("\tSignup process is cancelled")
                        print("\tYou'll be taken back")
                        return "Fail", []
                    else:
                        print("\tYou'll be taken further")
                        break

            while True:
                level = input("\n\tLevel: ")
                edit = input("\tDo you want to edit it? (Y/N): ")
                cancel = input("\tDo you want to cancel the signup process? (Y/N): ")
                if edit.lower() == 'y':
                    print("\tYou'll be allowed to edit")
                else:
                    if cancel.lower() == 'y':
                        print("\tSignup process is cancelled")
                        print("\tYou'll be taken back")
                        return "Fail", []
                    else:
                        print("\tYou'll be taken further")
                        break

        elif role == 'Non-Teacher':
            while True:
                type = input("\n\tType of Non-teaching staff: ")
                edit = input("\tDo you want to edit it? (Y/N): ")
                cancel = input("\tDo you want to cancel the signup process? (Y/N): ")
                if edit.lower() == 'y':
                    print("\tYou'll be allowed to edit")
                else:
                    if cancel.lower() == 'y':
                        print("\tSignup process is cancelled")
                        print("\tYou'll be taken back")
                        return "Fail", []
                    else:
                        print("\tYou'll be taken further")
                        break

            while True:
                staff_role = input(f"\n\tRole in {type} (Capital letters only): ")
                edit = input("\tDo you want to edit it? (Y/N): ")
                cancel = input("\tDo you want to cancel the signup process? (Y/N): ")
                if edit.lower() == 'y':
                    print("\tYou'll be allowed to edit")
                else:
                    if cancel.lower() == 'y':
                        print("\tSignup process is cancelled")
                        print("\tYou'll be taken back")
                        return "Fail", []
                    else:
                        print("\tYou'll be taken further")
                        break

        while True:
            email = input("\n\tE-mail: ")
            edit = input("\tDo you want to edit it? (Y/N): ")
            cancel = input("\tDo you want to cancel the signup process? (Y/N): ")
            if edit.lower() == 'y':
                print("\tYou'll be allowed to edit")
            else:
                if cancel.lower() == 'y':
                    print("\tSignup process is cancelled")
                    print("\tYou'll be taken back")
                    return "Fail", []
                else:
                    print("\tYou'll be taken further")
                    break

        edit = input("\n\tDo you want to edit your Personal Information? (Y/N): ")
        if edit.lower() == 'y':
            print("\tYou'll be allowed to edit your Personal Information")
            print("\tYou'll be taken back")
        else:
            print("\tYou'll be taken further")
            break

    cancel = input("\tDo you want to cancel the signup process? (Y/N): ")
    if cancel.lower() == 'y':
        print("\tSignup process is cancelled")
        print("\tYou'll be taken back")
        return "Fail", []

    info.append(name)
    if role == 'Student':
        info.append(clss)
        info.append(sec)
    elif role == 'Teacher':
        info.append(sub)
        info.append(level)
    elif role == 'Non-Teacher':
        info.append(type)
        info.append(staff_role)
    info.append(email)

    user_id = generate(root, name)
    info.append(user_id)
    info.append(role)

    with open(root, 'a', newline='') as f:
        write = csv.writer(f)
        write.writerow(info)

    return "Success", []


def display_table(data, title):
    if data == []:
        print("\tNo Events/Circular/Notice is currently there")
    else:
        print(tabulate(data, headers=title, tablefmt='pretty'))


def obtain_table_data():
    table_data = []
    with open("C:\\Users\\97150\\Projects\\Data\\table_data.csv") as f:
        x = -1
        read = csv.reader(f)
        for i in read:
            x += 1
            if x == 0:
                heads = i
            else:
                table_data.append(i)
    return table_data, heads


def order(data, def_ord='2'):
    if data == []:
        return data
    temp = copy.deepcopy(data)
    if def_ord == '2':
        latest = temp[::-1]
        x = 1
        for i in latest:
            i[0] = str(x)
            x = x + 1
        return latest
    elif def_ord == '1':
        oldest = org_data
        return oldest


def filter_table(table_data, def_filter='3'):
    temp = copy.deepcopy(table_data)
    filtered_table = []
    if def_filter == '1':
        print("\n\n\tFilter 'Types' in the following ways:")
        print("\t1. Event")
        print("\t2. Circular")
        print("\t3. Notice")
        print("\t4. You may press any other key to cancel")
        inp_3 = input("\tChoose (Enter number only): ")
        flag = False
        if inp_3 == '1':
            x = 1
            for i in temp:
                if i[2] == 'Event':
                    i[0] = str(x)
                    x += 1
                    filtered_table.append(i)
            flag = True
        elif inp_3 == '2':
            x = 1
            for i in temp:
                if i[2] == 'Circular':
                    i[0] = str(x)
                    x += 1
                    filtered_table.append(i)
            flag = True
        elif inp_3 == '3':
            x = 1
            for i in temp:
                if i[2] == 'Notice':
                    i[0] = str(x)
                    x += 1
                    filtered_table.append(i)
            flag = True
        if flag == True:
            return filtered_table
        else:
            return temp
    elif def_filter == '2':
        print("\n\n\tFilter 'Issued By' in the following ways:")
        print("\t1. Teachers")
        print("\t2. Students")
        print("\t3. Non-Teachers")
        print("\t4. Teachers/Non-Teachers")
        print("\t5. You may press any other key to cancel")
        inp_3 = input("\tChoose (Enter number only): ")
        flag = False
        if inp_3 == '1':
            x = 1
            for i in temp:
                if i[4] == 'Teachers':
                    i[0] = str(x)
                    x += 1
                    filtered_table.append(i)
            flag = True
        elif inp_3 == '2':
            x = 1
            for i in temp:
                if i[4] == 'Students':
                    i[0] = str(x)
                    x += 1
                    filtered_table.append(i)
            flag = True
        elif inp_3 == '3':
            x = 1
            for i in temp:
                if i[4] == 'Non-Teachers':
                    i[0] = str(x)
                    x += 1
                    filtered_table.append(i)
            flag = True
        elif inp_3 == '4':
            x = 1
            for i in temp:
                if i[4] == 'Teachers/Non-Teachers':
                    i[0] = str(x)
                    x += 1
                    filtered_table.append(i)
            flag = True
        if flag == True:
            return filtered_table
        else:
            return temp
    else:
        return temp


def search_by_sno(table_data, search_value):
    flag = False
    for i in table_data:
        if search_value == i[0]:
            flag = True
            name = i[1].replace(" ", '_')
            fname = "C:\\Users\\97150\\Projects\\Data" + "\\" + name + '.csv'
            with open(fname, 'r') as f:
                read = csv.reader(f)
                x = 0
                for j in read:
                    if x == 0:
                        x += 1
                        continue
                    else:
                        info = j
            if i[2] == 'Event':
                print(f"\n------{info[0].upper()}------")
                print(f"\nDate of Issue: {info[1]}", end='\t')
                print(f"Date of Event: {info[5]}")
                print(f"\n{info[4]}")
                print(f"\nIssued By: {info[3]}")
            else:
                print(f"\n------{i[2].upper()}------")
                print(f"\n------{info[0].upper()}------")
                print(f"\nDate of Issue: {info[1]}")
                print(f"\n{info[4]}")
                print(f"\nIssued By: {info[3]}")
            break
    return flag


def search_by_title(table_data, search_title):
    flag = False
    for i in table_data:
        if search_title.lower() == i[1].lower():
            flag = True
            name = i[1].replace(" ", '_')
            fname = "C:\\Users\\97150\\Projects\\Data" + "\\" + name + '.csv'
            with open(fname, 'r') as f:
                read = csv.reader(f)
                x = 0
                for j in read:
                    if x == 0:
                        x += 1
                        continue
                    else:
                        info = j
            if i[2] == 'Event':
                print(f"\n------{info[0].upper()}------")
                print(f"\nDate of Issue: {info[1]}", end='\t')
                print(f"Date of Event: {info[5]}")
                print(f"\n{info[4]}")
                print(f"\nIssued By: {info[3]}")
            else:
                print(f"\n------{info[0].upper()}------")
                print(f"\nDate of Issue: {info[1]}")
                print(f"\n{info[4]}")
                print(f"\nIssued By: {info[3]}")
            break
    return flag


def event_post(role, name, titles):
    event_info = []
    table_info = []
    print("\n\n\t\t\t------RULES------")
    print("\tYou've officially entered the posting page")
    print("\t1. You will be given a chance to edit or cancel the Posting process")
    print("\t2. Please be aware while Typing")
    print("\t3. You'll be taken further")
    time.sleep(8)

    while True:
        title = input("\tTitle of the Event: ")
        edit = input("\tDo you want to edit it? (Y/N): ")
        if edit.lower() == 'y':
            continue
        else:
            break
    cancel = input("\tDo you want to cancel the Posting process? (Y/N): ")
    if cancel.lower() == 'y':
        return 'Fail'

    while True:
        doi = input("\n\tDate of Issue (DD/MM/YYYY): ")
        edit = input("\tDo you want to edit it? (Y/N): ")
        if edit.lower() == 'y':
            print("\tYou'll be allowed to edit")
            continue
        else:
            check = True
            x = [1, 1, 2000]
            y = [32, 13, 3000]
            z = 0
            for j in doi.split('/'):
                if int(j) in range(x[z], y[z]):
                    z += 1
                    continue
                else:
                    check = False
                    break
            if check == False:
                print("\tEntered date is invalid")
            else:
                break

    cancel = input("\tDo you want to cancel the Posting process? (Y/N): ")
    if cancel.lower() == 'y':
        return "Fail"

    while True:
        print("\n\n\tNOTE:- PLEASE READ THE RULES FOR ENTERING DESCRIPTION")
        print("\t1. You'll be given 'n' no. of chances to type")
        print("\t2. You can use the enter key to go to the next line")
        print("\t3. You can enter 'n' no. of paras and lines")
        print("\t4. You cannot edit it")
        print("\t5. Please beware while typing")
        time.sleep(10)
        description = ""
        para = ""
        x = 1
        y = 1
        check = True
        while True:
            info = input(f"\n\tEnter line {x} of para {y}: ")
            print("\t1. Next line")
            print("\t2. Next Paragraph")
            print("\t3. Finish Typing")
            print("\t4. Cancel Typing or Retype from Starting")
            inp_4 = input("\tChoose (Enter number only): ")
            para = para + info + "\n"
            if inp_4 == '1':
                x += 1
            elif inp_4 == '2':
                description = description + para + '\n'
                para = ""
                y += 1
                x = 1
            elif inp_4 == '3':
                if y == 1:
                    description = para
                else:
                    description = description + para
                print("\n\tYou've finished typing")
                print("\tText is saved\n")
                break
            elif inp_4 == '4':
                print("\tText is not saved\n")
                check = False
                break

        if check == False:
            continue
        if check == True:
            break

    cancel = input("\tDo you want to cancel the Posting process? (Y/N): ")
    if cancel.lower() == 'y':
        return "Fail"

    while True:
        doe = input("\n\tDate of Event (DD/MM/YYYY): ")
        edit = input("\tDo you want to edit it? (Y/N): ")
        if edit.lower() == 'y':
            print("\tYou'll be allowed to edit")
            continue
        else:
            check = True
            x = [1, 1, 2000]
            y = [32, 13, 3000]
            z = 0
            for j in doe.split('/'):
                if int(j) in range(x[z], y[z]):
                    z += 1
                    continue
                else:
                    check = False
                    break
            if check == False:
                print("\tEntered date is invalid")
            else:
                break

    cancel = input("\tDo you want to cancel the Posting process? (Y/N): ")
    if cancel.lower() == 'y':
        return "Fail"

    print("\n\tThis is how your post will appear\n")
    print(f"---------{title.upper()}---------")
    print(f"\nDate of Issue: {doi}", end='\t')
    print(f"Date of Event: {doe}")
    print(f"\n{description}")
    print(f"\nIssued By: {name}")

    cancel = input("\tDo you want to cancel the Posting process? (Y/N): ")
    if cancel.lower() == 'y':
        return "Fail"

    event_info += [title.title(), doi, role, name, description, doe]
    table_info += [title.title(), 'Event', doi, role]

    with open('C:\\Users\\97150\\Projects\\Data\\table_data.csv', 'r') as f:
        read = csv.reader(f)
        x = -1
        for i in read:
            x += 1

    table_info.insert(0, str(x))

    with open('C:\\Users\\97150\\Projects\\Data\\table_data.csv', 'a', newline='') as f:
        write = csv.writer(f)
        write.writerow(table_info)

    name = title.replace(" ", "_")
    fname = "C:\\Users\\97150\\Projects\\Data" + "\\" + name + '.csv'

    with open(fname, 'w', newline='') as f:
        write = csv.writer(f)
        write.writerows([titles, event_info])

    return "Success"


def notice_post(role, name, titles):
    notice_info = []
    table_info = []
    print("\n\n\t\t\t------RULES------")
    print("\tYou've officially entered the posting page")
    print("\t1. You will be given a chance to edit or cancel the Posting process")
    print("\t2. Please be aware while Typing")
    print("\t3. You'll be taken further")
    time.sleep(8)

    while True:
        title = input("\tTitle of the Notice: ")
        edit = input("\tDo you want to edit it? (Y/N): ")
        if edit.lower() == 'y':
            continue
        else:
            break
    cancel = input("\tDo you want to cancel the Posting process? (Y/N): ")
    if cancel.lower() == 'y':
        return 'Fail'

    while True:
        doi = input("\n\tDate of Issue (DD/MM/YYYY): ")
        edit = input("\tDo you want to edit it? (Y/N): ")
        if edit.lower() == 'y':
            print("\tYou'll be allowed to edit")
            continue
        else:
            check = True
            x = [1, 1, 2000]
            y = [32, 13, 3000]
            z = 0
            for j in doi.split('/'):
                if int(j) in range(x[z], y[z]):
                    z += 1
                    continue
                else:
                    check = False
                    break
            if check == False:
                print("\tEntered date is invalid")
            else:
                break

    cancel = input("\tDo you want to cancel the Posting process? (Y/N): ")
    if cancel.lower() == 'y':
        return "Fail"

    while True:
        print("\n\n\tNOTE:- PLEASE READ THE RULES FOR ENTERING DESCRIPTION")
        print("\t1. You'll be given 'n' no. of chances to type")
        print("\t2. You can use the enter key to go to the next line")
        print("\t3. You can enter 'n' no. of paras and lines")
        print("\t4. You cannot edit it")
        print("\t5. Please beware while typing")
        time.sleep(10)
        description = ""
        para = ""
        x = 1
        y = 1
        check = True
        while True:
            info = input(f"\n\tEnter line {x} of para {y}: ")
            print("\t1. Next line")
            print("\t2. Next Paragraph")
            print("\t3. Finish Typing")
            print("\t4. Cancel Typing or Retype from Starting")
            inp_4 = input("\tChoose (Enter number only): ")
            para = para + info + "\n"
            if inp_4 == '1':
                x += 1
            elif inp_4 == '2':
                description = description + para + '\n'
                para = ""
                y += 1
                x = 1
            elif inp_4 == '3':
                if y == 1:
                    description = para
                else:
                    description = description + para
                print("\n\tYou've finished typing")
                print("\tText is saved\n")
                break
            elif inp_4 == '4':
                print("\tText is not saved\n")
                check = False
                break

        if check == False:
            continue
        if check == True:
            break

    cancel = input("\tDo you want to cancel the Posting process? (Y/N): ")
    if cancel.lower() == 'y':
        return "Fail"

    print("\n\tThis is how your post will appear")
    print(f"---------{title.upper()}---------")
    print(f"\nDate of Issue: {doi}", end='\t')
    print(f"\n{description}")
    print(f"\nIssued By: {name}")

    cancel = input("\tDo you want to cancel the Posting process? (Y/N): ")
    if cancel.lower() == 'y':
        return "Fail"

    notice_info += [title.title(), doi, role, name, description]
    table_info += [title.title(), 'Notice', doi, role]

    with open('C:\\Users\\97150\\Projects\\Data\\table_data.csv', 'r') as f:
        read = csv.reader(f)
        x = -1
        for i in read:
            x += 1

    table_info.insert(0, str(x))

    with open('C:\\Users\\97150\\Projects\\Data\\table_data.csv', 'a', newline='') as f:
        write = csv.writer(f)
        write.writerow(table_info)

    name = title.replace(" ", "_")
    fname = "C:\\Users\\97150\\Projects\\Data" + "\\" + name + '.csv'

    with open(fname, 'w', newline='') as f:
        write = csv.writer(f)
        write.writerows([titles, notice_info])

    return "Success"


def circular_post(role, name, titles):
    circular_info = []
    table_info = []
    print("\n\n\t\t\t------RULES------")
    print("\tYou've officially entered the posting page")
    print("\t1. You will be given a chance to edit or cancel the Posting process")
    print("\t2. Please be aware while Typing")
    print("\t3. You'll be taken further")
    time.sleep(8)

    while True:
        title = input("\tTitle of the Circular: ")
        edit = input("\tDo you want to edit it? (Y/N): ")
        if edit.lower() == 'y':
            continue
        else:
            break
    cancel = input("\tDo you want to cancel the Posting process? (Y/N): ")
    if cancel.lower() == 'y':
        return 'Fail'

    while True:
        doi = input("\n\tDate of Issue (DD/MM/YYYY): ")
        edit = input("\tDo you want to edit it? (Y/N): ")
        if edit.lower() == 'y':
            print("\tYou'll be allowed to edit")
            continue
        else:
            check = True
            x = [1, 1, 2000]
            y = [32, 13, 3000]
            z = 0
            for j in doi.split('/'):
                if int(j) in range(x[z], y[z]):
                    z += 1
                    continue
                else:
                    check = False
                    break
            if check == False:
                print("\tEntered date is invalid")
            else:
                break

    cancel = input("\tDo you want to cancel the Posting process? (Y/N): ")
    if cancel.lower() == 'y':
        return "Fail"

    while True:
        print("\n\n\tNOTE:- PLEASE READ THE RULES FOR ENTERING DESCRIPTION")
        print("\t1. You'll be given 'n' no. of chances to type")
        print("\t2. You can use the enter key to go to the next line")
        print("\t3. You can enter 'n' no. of paras and lines")
        print("\t4. You cannot edit it")
        print("\t5. Please beware while typing")
        time.sleep(10)
        description = ""
        para = ""
        x = 1
        y = 1
        check = True
        while True:
            info = input(f"\n\tEnter line {x} of para {y}: ")
            print("\t1. Next line")
            print("\t2. Next Paragraph")
            print("\t3. Finish Typing")
            print("\t4. Cancel Typing or Retype from Starting")
            inp_4 = input("\tChoose (Enter number only): ")
            para = para + info + "\n"
            if inp_4 == '1':
                x += 1
            elif inp_4 == '2':
                description = description + para + '\n'
                para = ""
                y += 1
                x = 1
            elif inp_4 == '3':
                if y == 1:
                    description = para
                else:
                    description = description + para
                print("\n\tYou've finished typing")
                print("\tText is saved\n")
                break
            elif inp_4 == '4':
                print("\tText is not saved\n")
                check = False
                break

        if check == False:
            continue
        if check == True:
            break

    cancel = input("\tDo you want to cancel the Posting process? (Y/N): ")
    if cancel.lower() == 'y':
        return "Fail"

    print("\n\tThis is how your post will appear")
    print(f"---------{title.upper()}---------")
    print(f"\nDate of Issue: {doi}", end='\t')
    print(f"\n{description}")
    print(f"\nIssued By: {name}")

    cancel = input("\tDo you want to cancel the Posting process? (Y/N): ")
    if cancel.lower() == 'y':
        return "Fail"

    circular_info += [title.title(), doi, role, name, description]
    table_info += [title.title(), 'Circular', doi, role]

    with open('C:\\Users\\97150\\Projects\\Data\\table_data.csv', 'r') as f:
        read = csv.reader(f)
        x = -1
        for i in read:
            x += 1

    table_info.insert(0, str(x))

    with open('C:\\Users\\97150\\Projects\\Data\\table_data.csv', 'a', newline='') as f:
        write = csv.writer(f)
        write.writerow(table_info)

    name = title.replace(" ", "_")
    fname = "C:\\Users\\97150\\Projects\\Data" + "\\" + name + '.csv'

    with open(fname, 'w', newline='') as f:
        write = csv.writer(f)
        write.writerows([titles, circular_info])

    return "Success"


def posting(user_role, user_name):
    heads1 = ['TITLE', 'DOI', 'ISSUED BY', 'AUTHOR/S', 'DESCRIPTION', 'DATE OF EVENT']
    heads2 = ['TITLE', 'DOI', 'ISSUED BY', 'AUTHOR/S', 'DESCRIPTION']
    print("\n\n\n\t\t\t------POST-------")
    if user_role == 'Student':
        print("\tYou can Post the following:")
        print("\t1. Event")
        print("\t2. Notice")
        print("\t3. You may press any other key to cancel")
        inp_2 = input("\tChoose (Enter number only): ")
        if inp_2 == '1':
            check = event_post(user_role, user_name, heads1)
        elif inp_2 == '2':
            check = notice_post(user_role, user_name, heads2)
        else:
            return False
    else:
        print("\tYou can Post the following:")
        print("\t1. Event")
        print("\t2. Circular")
        print("\t3. Notice")
        print("\t4. You may press any other key to cancel")
        inp_2 = input("\tChoose (Enter number only): ")
        if inp_2 == '1':
            check = event_post(user_role, user_name, heads1)
        elif inp_2 == '2':
            check = circular_post(user_role, user_name, heads2)
        elif inp_2 == '3':
            check = notice_post(user_role, user_name, heads2)
        else:
            return False
    if check == 'Fail':
        return False
    else:
        return True


def view_acc_info(info):
    print("\n\n\n\t\t------ACCOUNT INFORMATION------")
    print(f"\tUsername: {info[1]}")
    print(f"\tPassword: {info[2]}")
    print(f"\tEmail: {info[6]}")
    print(f"\tUser ID: {info[7]}")
    print(f"\tRole: {info[8]}")


def view_per_info(info):
    print("\n\n\n\t\t\t------PEROSNAL INFOMRATION------")
    print(f"\tName: {info[3]}")
    if info[8] == 'Student':
        print(f"\tClass: {info[4]}")
        print(f"\tSection: {info[5]}")
    elif info[8] == 'Teacher':
        print(f"\tSubject: {info[4]}")
        print(f"\tLevel; {info[5]}")
    else:
        print(f"\tType: {info[4]}")
        print(f"\t Staff Role: {info[5]}")


# Main Program
print("\t------EVENT MANAGEMENT SYSTEM------")
while True:
    print("\n\t\t\t------WELCOME------")
    print("\n\t1. Login/Signup")
    print("\t2. Exit Application")
    inp_main = input("\tChoose (Enter number only): ")

    # Displaying Login/Signup Interface
    if inp_main == '1':
        while True:
            print("\n\n\n\t\t---------LOGIN/SIGNUP---------")
            print("\n\t1. Login\n\t2. Signup\n\t3. Exit")
            inp_1 = input("\tChoose (Enter number only): ")

            if inp_1 == '1':
                while True:
                    print("\n\n\n\t\t------LOGIN------")
                    print("\n\t1. Student")
                    print("\t2. Teacher")
                    print("\t3. Non-Teacher")
                    print("\t4. Exit")
                    inp_2 = input("\tChoose (Enter number only): ")

                    if inp_2 == '1':
                        file_name = r'C:\Users\97150\Projects\Data\student_info.csv'
                        check, user_info = login(file_name, inp_2)
                        break

                    elif inp_2 == '2':
                        file_name = r'C:\Users\97150\Projects\Data\teacher_info.csv'
                        check, user_info = login(file_name, inp_2)
                        break

                    elif inp_2 == '3':
                        file_name = r'C:\Users\97150\Projects\Data\non_teacher_info.csv'
                        check, user_info = login(file_name, inp_2)
                        break

                    else:
                        print("\tInvalid Option entered")
                        print("\tPlease enter a valid option\n\n\n")

            elif inp_1 == '2':
                while True:
                    print("\n\n\n\t\t------SIGNUP------")
                    print("\n\t1. Student")
                    print("\t2. Teacher")
                    print("\t3. Non-Teacher")
                    print("\t4. Exit")
                    inp_2 = input("\tChoose (Enter number only): ")

                    if inp_2 == '1':
                        file_name = r'C:\Users\97150\Projects\Data\student_info.csv'
                        check, user_info = signup(file_name, inp_2)
                        break

                    elif inp_2 == '2':
                        file_name = r'C:\Users\97150\Projects\Data\teacher_info.csv'
                        check, user_info = signup(file_name, inp_2)
                        break

                    elif inp_2 == '3':
                        file_name = r'C:\Users\97150\Projects\Data\non_teacher_info.csv'
                        check, user_info = signup(file_name, inp_2)
                        break

                    else:
                        print("\tInvalid Option entered")
                        print("\tPlease enter a valid option\n\n\n")

            elif inp_1 == '3':
                print("\tYou'll be taken back\n\n\n")
                flag = False
                break

            else:
                print("\tInvalid Option entered")
                print("\tPlease enter a valid option\n\n\n")
                continue

            if check == "Success":
                if user_info == []:
                    print("\tYou've successfully signed up")
                    print("\tYou may Login\n\n\n")
                    continue
                else:
                    print("\tYou've successfully logged in")
                    print("\tYou'll be taken to the Home page")
                    flag = True
                    break
            elif check == "Fail":
                print("\tYou'll be taken back to the Login/Signup Page")
                continue

    elif inp_main == '2':
        print("\tThank you for opening our application")
        print("\tThe app will be closed shortly")
        time.sleep(2)
        sys.exit()

    else:
        print("\tInvalid Option entered")
        print("\tPlease enter a valid option\n\n\n")
        continue

    if flag == True:
        org_data, heads = obtain_table_data()
        user_order = order(org_data)
        while True:
            print("\n\n\n\t\t\t\t------------HOME------------")
            print("\t\t\t\t\t-------RECENT-------")
            display_table(user_order, heads)
            print("\t1. Search")
            print("\t2. Sort")
            print("\t3. Filter")
            print("\t4. Post")
            print("\t5. Settings")
            print("\tNOTE:- YOU CAN EITHER SORT OR FILTER ONLY, NOT BOTH!!!")
            inp_1 = input("\tChoose (Enter number only): ")
            if inp_1 == '1':
                while True:
                    print("\n\n\n\t\t\t------SEARCH------")
                    print("\tFollowing are the ways to Search:")
                    print("\t1. Search by SNo.")
                    print("\t2. Search by Title")
                    print("\t3.You may press any other key to cancel")
                    inp_2 = input("\tChoose (Enter number only): ")
                    if inp_2 == '1':
                        inp_3 = input("\n\n\tChoose (Enter SNo. from above table): ")
                        check = search_by_sno(user_order, inp_3)
                        time.sleep(15)
                    elif inp_2 == '2':
                        inp_3 = input("\n\n\tChoose (Enter Title from above table): ")
                        check = search_by_title(user_order, inp_3)
                        time.sleep(15)
                    else:
                        break
                    if flag == False:
                        print("\n\n\tNo Such Event/Circular/Notice found")
                        print("\tPlease enter a Valid Event/Circular/Notice")
            elif inp_1 == '2':
                while True:
                    user_order = order(org_data)
                    print("\n\n\tSort in the following orders:")
                    print("\t1. Date of Issue (Oldest First)")
                    print("\t2. Date of Issue (Latest First)")
                    print("\t3. You may press any other key to cancel")
                    inp_2 = input("\tChoose (Enter number only): ")
                    if inp_2 == '1':
                        user_order = order(user_order, inp_2)
                        break
                    elif inp_2 == '2':
                        user_order = order(user_order, inp_2)
                        break
                    else:
                        break
            elif inp_1 == '3':
                while True:
                    print("\n\n\tFilter the following from the table:")
                    print("\t1. Type")
                    print("\t2. Issued By")
                    print("\t3. Return to Original")
                    print("\t4. You may press any other key to cancel")
                    inp_2 = input("\tChoose (Enter number only): ")
                    if inp_2 == '1':
                        user_order = filter_table(org_data, inp_2)
                        break
                    elif inp_2 == '2':
                        user_order = filter_table(org_data, inp_2)
                        break
                    elif inp_2 == '3':
                        user_order = order(org_data)
                        break
                    else:
                        break
            elif inp_1 == '4':
                while True:
                    role = user_info[8]
                    name = user_info[3]
                    check = posting(role, name)
                    if check == False:
                        print("\n\tYou've Not Posted")
                        print("\tYou'll be taken back")
                        org_data, heads = obtain_table_data()
                        user_order = order(org_data)
                        break
                    elif check == True:
                        print("\n\tYou've Successfully Posted")
                        print("\tYou'll be taken back")
                        org_data, heads = obtain_table_data()
                        user_order = order(org_data)
                        break

            elif inp_1 == '5':
                flag = False
                while True:
                    print("\n\n\n\t\t\t------SETTINGS------")
                    print("\t1. View Account Information")
                    print("\t2. View Personal Information")
                    print("\t3. Logout")
                    print("\t4. Exit")
                    inp_2 = input("\tChoose (Enter number only): ")
                    if inp_2 == '1':
                        view_acc_info(user_info)
                        time.sleep(5)
                    elif inp_2 == '2':
                        view_per_info(user_info)
                        time.sleep(5)
                    elif inp_2 == '3':
                        logout = input("\tAre you sure to logout? (Y/N): ")
                        if logout.lower() == 'y':
                            flag = True
                            print("\tYou'll be Logged out\n")
                            break
                        else:
                            time.sleep(5)
                    elif inp_2 == '4':
                        print("\tYou'll be taken back to the Home page")
                        break
                    else:
                        print("\tInvalid Option entered")
                        print("\tPlease enter a Valid Option")
                if flag == True:
                    break


