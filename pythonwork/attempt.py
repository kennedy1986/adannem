username = input("enter user name:\n")
password = ""
attempt = 0
flag = 0
while attempt != 3:
    password = input("enter your password:")
    if password == "admin":
        flag = 1
        break
    else:
        attempt = attempt +1
        if attempt == 3:
            print("you have tried maximium times")
if flag == 1:
    print("welcome " + username)
