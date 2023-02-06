users = {"Gargee":"123", "Akshay":"456", "prof":"789"}
owners = {"owner1": "abc", "owner2":"xyz", "owner3":"efg"}
admin = {"admin": "123"}

Users_Names=[]
for name,password in users.items():
    Users_Names.append(name)

for name,password in owners.items():
    Users_Names.append(name)

for name,password in admin.items():
    Users_Names.append(name)

dict1={}

for i in range(0,len(Users_Names),1):
    dict1[Users_Names[i]] = list()
    

def authenticate():
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
def message(Current_User):
    msg_service = ['Check Messages','Send a message to user']
    print("\nPlease Select an option:")
    j=1
    for i in msg_service:
        print(j,": " ,i)
        j+=1
    opt=int(input())
    if opt == 1:
        print("Messages for ",Current_User,"\n")
        print(dict1[Current_User])
    
    elif opt==2:
        print("Please Select a Role to Send a message")
        roles =["User","Owner","Admin"]
        j=1
        for i in roles:
            print(j,": ",i)
            j+=1
        msg_role=int(input())
        if(msg_role == 1):
            print("Please Enter the name of the available User ")
            for name,password in users.items():
                print(name)
            Select_User = input()
            print(Select_User)
            print("Please type in the message to send to ",Select_User)
            input_message=input()
            dict1[Select_User].append(input_message)
            print(dict1)
        elif(msg_role == 2):
            print("Please Enter the name of the available Owner ")
            for name,password in owners.items():
                print(name)
            Select_User = input()
            print("Please type in the message to send to ",Select_User)
            input_message=input()
        elif(msg_role == 3):
            print("Please Enter the name of the Admin")
            for name,password in admin.items():
                print(name)
            Select_User = input()
            print("Please type in the message to send to ",Select_User)
            input_message=input()
        
            
    

if __name__ == '__main__':
    
    print("Hello, Welcome to our seat booking application!\n")
    
    role = authenticate()
    Current_User = role.split('_')
    Current_User = Current_User[1]
    print(f"Welcome {role.split('_')[1]}!")
    
    options=['New Reservation', 'Existing Reservation', 'Check Inbox']
    print("\nPlease select:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    selected_option = int(input("\nEnter your choice: "))
    choice = selected_option
    if(choice == 3):
        message(Current_User)
