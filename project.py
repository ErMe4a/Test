DB_EMAILS = []

while True:
    print('1) Input Emails      2) Show DB_Emails 3)del e-mail  4)Stop 5)rename email')
    choices = int(input("Enter choices: " ))
    if choices ==1:
        email = input("Enter emails: ")
        
        if "@gmail.com" in email:   # if email.endswith("@gmail.com"):   DB_EMAILS.append(email) continue  print("invalid emails")
            if email in DB_EMAILS:
                print("This e-mail registered in e-mail")
                continue
            DB_EMAILS.append(email)
            continue
        print("Error")
    elif choices == 2:
        print(DB_EMAILS)
    elif choices ==3:
        email = input("enter email: ")
        if email in DB_EMAILS:
            # index = DB_EMAILS.index(email)
            # DB_EMAILS.pop(index)
            DB_EMAILS.remove(email)
        else:
            print(f"{email} not exist")    
    elif choices ==4:
        break
    elif choices == 5:
        old_email = input("Enter email:")
        if old_email in DB_EMAILS:
            new_email = input("enter new email: ")
            if "@gmail.com" in email:   # if email.endswith("@gmail.com"):   DB_EMAILS.append(email) continue  print("invalid emails")
                if new_email in DB_EMAILS:
                    print("This e-mail registered in e-mail")
                    continue
                DB_EMAILS.remove(old_email)    
                DB_EMAILS.append(new_email)
            
    else:
        print("Error")    
