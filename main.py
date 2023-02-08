import math
import numpy as np

users = {"Gargee":"123", "Akshay":"456", "prof":"789"}
owners = {"owner1": "abc", "owner2":"xyz", "owner3":"efg"}
admin = {"admin": "123"}

class owner:
    def __init__(self, service, size, price,messages):
        self.size = size
        self.price = price
        self.messages = messages
        self.service = service
    
    def set_price(self):
        if self.size==1:
            self.square_array = np.full((size,size), 2*self.price, dtype=int)
        elif self.size ==2:
            self.square_array = np.full((size,size), self.price, dtype=int)
            self.square_array[0,:] = 2*self.price
        elif self.size == 3:
            self.square_array = np.full((size,size), self.price, dtype=int)
            self.square_array[0,:] = 2*self.price
            self.square_array[size-1,:]=0.75*self.price
            self.square_array[1:size-1,int(size/2)]=1.25*self.price 
        else:
            self.square_array = np.full((size,size), self.price, dtype=int)
            self.square_array[0,:] = 2*self.price
            self.square_array[size-1,:]=0.75*self.price
            self.square_array[1:size-1,int(size/2)-1:int(size/2)+1]=1.25*self.price 
        return self.square_array

    def get_messages(self):
        return(self.messages)

    def select_dates(self):
        print("Please select dates:")
        options = ["1/1/23", "2/1/23", "3/1/23", "4/1/23"]
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        selected_options = set(map(int, input("Enter your choices (separated by spaces): ").split()))
        selected_options = [options[i-1] for i in selected_options if i > 0 and i <= len(options)]
        return selected_options

    def select_times(self):
        print("Please select times:")
        options = ["18:00", "19:00", "20:00", "21:00"]
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        selected_options = set(map(int, input("Enter your choices (separated by spaces): ").split()))
        selected_options = [options[i-1] for i in selected_options if i > 0 and i <= len(options)]
        return selected_options
    
def get_owner_details():
    service=str(input("\nEnter Service: "))
    size = int(input("\nEnter size of the room: "))
    reg_price = int(input("\nEnter regular price: "))
    return service, size, reg_price


class user:
    #def __init__(self, service, seat_id, date, time, business_class, messages):
    def __init__(self):
        self.booked_seat = None
    
    def get_action(self, user):
        options=['New Reservation', 'Existing Reservation', 'Check Inbox']
        print("\nPlease select:")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        selected_option = int(input("\nEnter your choice: "))
        choice = selected_option
        if choice==1:
            u.book_seat()
        if choice==2:
            option = ['Cancel Ticket', 'Sell Ticket', 'Exchange Ticket']
            print("\nPlease select:")
            for i, option in enumerate(option):
                print(f"{i+1}. {option}")
            selected_option = int(input("\nEnter your choice: "))
            choice = option[selected_option-1]
            if choice == 1: u.cancel_booking
            if choice == 2: u.sell_seat
            if choice==3: u.change_booking
        if(choice == 3):
            message(user)

        
    def book_seat(self, seat):
        self.booked_seat = seat #new and sell list
    
    def change_booking(self, new_seat):
        self.booked_seat = new_seat
    
    def cancel_booking(self):
        self.booked_seat = None
    
    def sell_seat(self, seat, sell_list):
        sell_list.add_seat(seat)
    
    def send_complaint(self, complaint, admin):
        admin.receive_complaint(complaint)

message_dict ={}
a = list(users.keys()); b = list(owners.keys()); c = list(admin.keys())
all_users=a+b+c

for i in all_users:
    message_dict[i] = []
    
def authenticate():
    global users, owners, admin
    while True:
        while True:
            username = str(input("Username: "))
            if username in users or username in owners or username in admin:
                password = str(input("Password: ")); 
            else: print("\nUser does not exist, Try again! \n"); 

            if username in users: 
                if users[username]==password: print("\nAuthentication Successful, Logging in"); role = "user_"+username; return role
                else: print("Incorrect password, try again")
            elif username in owners:
                if owners[username]==password: print("\nAuthentication Successful, Logging in"); role = "owner_"+username; return role
                else: print("Incorrect password, try again")
            elif username in admin: 
                if admin[username]==password: print(("\nAuthentication Successful, Logging in")); role = "admin"; return role
                else: print("Incorrect password, try again")

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
        print(message_dict[Current_User])
    
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
            message_dict[Select_User].append(input_message)
            print(message_dict)
        elif(msg_role == 2):
            print("Please Enter the name of the available Owner ")
            for name,password in owners.items():
                print(name)
            Select_User = input()
            print("Please type in the message to send to ",Select_User)
            input_message=input()
            message_dict[Select_User].append(input_message)
            print(message_dict)
        elif(msg_role == 3):
            print("Please Enter the name of the Admin")
            for name,password in admin.items():
                print(name)
            Select_User = input()
            print("Please type in the message to send to ",Select_User)
            input_message=input()
            message_dict[Select_User].append(input_message)
            
        
            
def msg_all(msg,current_user):
    for user in all_users:
        if(current_user != user):
            message_dict[user].append(msg)

if __name__ == '__main__':
    while True:
        print("Hello, Welcome to our seat booking application!\n")
        print("Please enter your login credentials")
        role = authenticate()
        name = role.split('_')[1]
        print(f"Welcome {name}!")

        if role.split('_')[0] == 'owner':

            if name not in owners:
                owners[name]={}
                service, size, reg_price = get_owner_details()
                owners[name][service]={}
                owners[name][service]['price']= [];owners[name][service]['dates'] =[]; owners[name][service]['times']=[]; owners[name]['messages'] =[]
                messages=[]
                ans=' '
            else:
                print('\n your existing room details are as follows: ')
                print("\n", owners[name])
                ans = str(input("\n If you want to add another room, press yes otherwise press q to exit"))
                if ans == 'q':
                    continue
                if ans=='yes':
                    service, size, reg_price = get_owner_details()
                    if service not in owners[name]:
                        owners[name][service]={}
                        owners[name][service]['price']= [];owners[name][service]['dates'] =[]; owners[name][service]['times']=[]; owners[name]['messages'] =[]


            o = owner(service, size, reg_price, messages)

            while ans != 'q':
                owners[name][service]['price'].append(o.set_price())
                owners[name][service]['dates'].append(o.select_dates())
                owners[name][service]['times'].append(o.select_times())
                owners[name]['messages'].append(o.get_messages())
                print("\n Your saved details: \n", owners[name])
                ans = str(input("\n If you want to add another room, enter yes \n if you want to view existing rooms, enter show\n otherwise press q to exit"))
                if ans == 'show':
                    print(owners[name])
                    ans = str(input("\n If you want to add another room, enter yes \n otherwise press q to exit"))
                if ans=='yes':
                    service, size, reg_price = get_owner_details()
            continue

        if role.split('_')[0] == 'user':
            u = user()
            while True:
                u.get_action(role.split('_')[1])
                ans = str(input("\n If you want to go back, enter b \n otherwise press q to exit"))
                if ans == 'b':
                    continue
                else:
                    break
        continue

