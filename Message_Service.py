users = {"Gargee":"123", "Akshay":"456", "prof":"789"}
owners = {"owner1": "abc", "owner2":"xyz", "owner3":"efg"}
admin = {"admin": "123"}

all_users=[]
complaints={}
for name,password in users.items():
    all_users.append(name)

for name,password in owners.items():
    all_users.append(name)

for name,password in admin.items():
    all_users.append(name)

message_dict={}
complaints={}

for i in range(len(all_users)):
    temp_user_list = all_users.copy() #i=Gargee
    temp_user_list.pop(i)
    message_dict[all_users[i]]={}
    for j in range(len(temp_user_list)): #j=prof
        message_dict[all_users[i]][temp_user_list[j]]=[]

for i in all_users:
    complaints[i]=''
#print(Users_Names)

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
        if admin[username]==password: print(("\nAuthentication Successful, Logging in")); role = "admin"+username; return role
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
        for i in message_dict[Current_User]:
            print(i,":") 
            inner_dict = message_dict[Current_User]
            #print("inner_dict ",inner_dict)
            message_list=inner_dict[i]
            #print("message_list ",message_list)
            for msg in message_list:
                print(msg)
                
    elif opt == 2:
        print("Select a User to send Message")
        for x in range(len(all_users)):
            if all_users[x] != Current_User:print(all_users[x])
        req_user = input()
        print("please type in a message to send to ",req_user)
        message=input()
        message_dict[req_user][Current_User].append(message)
        
            
def msg_all(msg,current_user):
    for user in all_users:
        if(current_user != user):
            message_dict[user][current_user].append(msg)
            
def  Complaintbox(user,role):
    if role == "admin":
        for key,value in complaints.items():
            print(key,value)
    else:
        complaint=input("Please tell me your concern so I can report it to the developers: \n")
        complaints[user]=complaint
            
            
    

if __name__ == '__main__':
    
    print("Hello, Welcome to our seat booking application!\n")
    
    role = authenticate()
    Current_User = role.split('_')
    Current_User_role=Current_User[0]
    Current_User = Current_User[1]
   
    print(f"Welcome {role.split('_')[1]}!")
    
    options=['New Reservation', 'Existing Reservation', 'Check Inbox','Report an issue','Publish a message']
    print("\nPlease select:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    selected_option = int(input("\nEnter your choice: "))
    choice = selected_option
    #print("Type a message to publish")
    #msg=input()
    #msg_all(msg,Current_User)
    if(choice == 3):
        message(Current_User)
    if(choice == 4):
        Complaintbox(Current_User, Current_User_role)
    if(choice == 5):
        msg=input("Please type a message to publish to all users   \n")
        msg_all(msg,Current_User)