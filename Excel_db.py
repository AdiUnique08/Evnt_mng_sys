# Testing Dataframe

import pandas as pd

# Reading excel file

userpass_xl = pd.read_excel(r'C:\Users\97150\PycharmProjects\Event_Mng_Sys\Account_Signin.xlsx')
print(userpass_xl)

# Converting dataframe into dictionary and making username: password pair.

userpass = dict(zip(userpass_xl.USERNAMES, userpass_xl.PASSWORD))
print(userpass)

# Taking inputs for username and password and updating dictionary

username = input("Please enter a username: ")
password = input("Please enter a password: ")
userpass_upd = {username: password}
userpass.update(userpass_upd)
print(f"New dictionary:\n{userpass}")

# Updating excel file by appending a new key value pair

userpass_xl = pd.DataFrame({"USERNAMES": userpass.keys(), "PASSWORD": userpass.values()})
print(userpass_xl)
with pd.ExcelWriter(r'C:\Users\97150\PycharmProjects\Event_Mng_Sys\Account_Signin.xlsx') as writer:
    userpass_xl.to_excel(writer, sheet_name='Userpass')
