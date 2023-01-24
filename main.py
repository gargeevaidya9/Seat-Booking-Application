def authenticate():
    users = {"Gargee":"123", "Akshay":"456", "prof":"789"}
    owners = {"owner1": "abc", "owner2":"xyz", "owner3":"efg"}
    admin = {"admin": "123"}

    username = str(input("Username: "))
    if username in users or username in owners or username in admin:
        password = str(input("Password: "))
    else: print("\nUser does not exist, Try again! \n"); authenticate()

    if username in users: 
        if users[username]==password: print("\nAuthentication Successful, Logging in"); role = "user_"+username; return role
    elif username in owners:
        if owners[username]==password: print("\nAuthentication Successful, Logging in"); role = "owner_"+username; return role
    elif username in admin: 
        if admin[username]==password: print(("\nAuthentication Successful, Logging in")); role = "admin"; return role
    else:
        print("Incorrect password, try again")
        authenticate()        

if __name__ == '__main__':
    
    print("Hello, Welcome to our seat booking application!\n")
    print("Please enter your login credentials")
    role = authenticate()
    print(f"Welcome {role.split('_')[1]}!")
    
  
    
