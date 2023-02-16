import math
import numpy as np
import getpass as gp
import copy

users = {"Gargee":"123", "Akshay":"456", "prof":"789"}
owners = {"owner1": "abc", "owner2":"xyz", "owner3":"efg"}
admin = {"admin": "123"}

message_dict ={}
a = list(users.keys()); b = list(owners.keys()); c = list(admin.keys())
all_users=a+b+c

complaints={}
for i in all_users:
    complaints[i]=''

for i in all_users:
    message_dict[i] = []

class owner:
    def __init__(self, service, size, price):
        self.size = size
        self.price = price
        #self.messages = messages
        self.service = service
    
    def set_price(self):
        if self.size==1:
            self.square_array = np.full((size,size), 2*self.price, dtype=float)
        elif self.size ==2:
            self.square_array = np.full((size,size), self.price, dtype=float)
            self.square_array[0,:] = 2*self.price
        elif self.size == 3:
            self.square_array = np.full((size,size), self.price, dtype=float)
            self.square_array[0,:] = 2*self.price
            self.square_array[size-1,:]=0.75*self.price
            self.square_array[1:size-1,int(size/2)]=1.25*self.price 
        else:
            self.square_array = np.full((size,size), self.price, dtype=float)
            self.square_array[0,:] = 2*self.price
            self.square_array[size-1,:]=0.75*self.price
            self.square_array[1:size-1,int(size/2)-1:int(size/2)+1]=1.25*self.price 
        return self.square_array

    #def get_messages(self):
    #    return(self.messages)

    def select_dates(self):
        while True:
            try:
                print("Please select dates:")
                options = ["1/1/23", "2/1/23", "3/1/23", "4/1/23"]
                for i, option in enumerate(options):
                    print(f"{i+1}. {option}")
                selected_opt = set(map(int, input("Enter your choices (separated by spaces): ").split()))
                selected_options = [options[i-1] for i in selected_opt if i > 0 and i <= len(options)]
                for i in selected_opt:
                    if int(i)>len(options) or int(i)<0:
                        print("Invalid choice try again")
                    else:
                        return selected_options
            except:
                print("Please enter an integer value")

    def select_times(self):
        while True:
            try:
                print("Please select times:")
                options = ["18:00", "19:00", "20:00", "21:00"]
                for i, option in enumerate(options):
                    print(f"{i+1}. {option}")
                selected_opt = set(map(int, input("Enter your choices (separated by spaces): ").split()))
                selected_options = [options[i-1] for i in selected_opt if i > 0 and i <= len(options)]
                for i in selected_opt:
                    if int(i)>len(options) or int(i)<0:
                        print("Invalid choice try again")
                    else:
                        return selected_options
            except:
                print("Please enter an integer value")
    
def get_owner_details():
    service=str(input("\nEnter Service: "))

    while True:
        try:
            size = int(input("\nEnter size of the room: "))
            if size>0:
                break
            else:
                print("size should be more than 0")
        except:
            print("size should be an integer, try again")
    
    while True:
        try:
            reg_price = int(input("\nEnter regular price: "))
            if reg_price>0:
                break
            else:
                print("Price should be more than $0, try again")
        except:
            print("price should be an integer, try again")
        
    return service, size, reg_price


class user:
    #def __init__(self, service, seat_id, date, time, business_class, messages):
    def __init__(self,name):
        self.name = name
    
    def get_action(self, available_rooms,booking_track,sell_list):
        options=['New Reservation', 'Existing Reservation', 'Check Inbox']
        print("\nPlease select:")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        while True:
                try:
                    selected_option = int(input("\nEnter your choice: "))
                    if selected_option>len(options) or selected_option<0 or type(selected_option) is not int:
                        print('Invalid choice, try again')
                    else:
                        break
                except:
                    print('Invalid choice, try again')
        choice = selected_option
        if choice==1:
            a,b,s = u.book_seat(available_rooms)
        if choice==2:
            option = ['Cancel Ticket', 'Sell Ticket', 'Exchange Ticket']
            print("\nPlease select:")
            for i, option in enumerate(option):
                print(f"{i+1}. {option}")
            while True:
                try:
                    selected_option = int(input("Enter your choice: "))
                    if selected_option>len(options) or selected_option<0 or type(selected_option) is not int:
                        print('Invalid choice, try again')
                    else:
                        break
                except:
                    print('Invalid choice, try again')
            choice = option[selected_option-1]
            if choice == 1: u.cancel_booking
            if choice == 2: u.sell_seat
            if choice==3: u.change_booking
        if(choice == 3):
            message(self.name)
        
        return a,b,s
        
        
    def book_seat(self, available_rooms):
        while True:
            print("\nAvailable services: ")
            options=[]
            for i in available_rooms.keys():
                for key in available_rooms[i]:
                    options.append(key)

            while True:
                if len(options)==0: 
                    print("No services available\n")
                    return available_rooms,booking_track,sell_list
                else:
                    break
            
            for a, option in enumerate(options):
                print(f"{a+1}. {option}")
            while True:
                try:
                    selected_option = int(input("\nselect service: "))
                    if selected_option>len(options) or selected_option<0 or type(selected_option) is not int:
                        print('Invalid choice, try again')
                    else:
                        break
                except: 
                    print('Invalid choice, try again')
                    continue
            self.service = options[selected_option-1]

            for i in available_rooms.keys():
                for key in available_rooms[i]:
                    if key==self.service:
                        owner_index = i
                        break
            
            print("Select date from the available date list\n")
            options_dates = available_rooms[owner_index][self.service]["dates"]
            for a, option in enumerate(options_dates):
                print(f"{a+1}. {option}")
            while True:
                try:
                    selected_option_date = int(input("Enter your choice: "))
                    if selected_option_date>len(options_dates) or selected_option_date<0:
                        print('Invalid choice, try again')
                    else:
                        break
                except:
                    continue
            self.date = options_dates[selected_option_date-1]

            print("Select time from the available time list\n")
            options_times = available_rooms[owner_index][self.service]["times"]
            for a, option in enumerate(options_times):
                print(f"{a+1}. {option}")
            while True:
                try:
                    selected_option_time = int(input("Enter your choice: "))
                    if selected_option_time>len(options_times) or selected_option_time<0:
                        print('Invalid choice, try again')
                    else:
                        break
                except:
                    print('Invalid choice, try again')
            self.time = options_times[selected_option_time-1]                

            red_flag=0
            for id in booking_track:
                    for serv in booking_track[id]:
                        if self.name in booking_track[id][serv]:
                            for i in booking_track[id][serv][self.name]:
                                if i.split('_')[1] == str(self.date) and i.split('_')[2] == str(self.time):
                                    print(f"You already have a reservation in this time slot for {serv}, please try again")
                                    red_flag = 1
            
            if red_flag==1:
                continue
            
            index = selected_option_date*selected_option_time-1
            while True:
                try:
                    print("Seat Layout with price for each seat (displayed top row is the 1st front row): \n")
                    print(available_rooms[owner_index][self.service]["price_for_each_seat"][index])
                    print("Seats marked None are unavailable for booking")
                    while True:
                        self.seat = str(input("\nSelect row,column desired seat (Separated by space): "))
                        row, col = int(self.seat.split(" ")[0]), int(self.seat.split(" ")[1])
                        check_shape= available_rooms[owner_index][self.service]["price_for_each_seat"][index].shape[0]
                        if row>check_shape or col>check_shape or row<=0 or col<=0:
                            print("Invalid seat choice, please try again")
                        else:
                            break
                    self.price = available_rooms[owner_index][self.service]["price_for_each_seat"][index][row-1,col-1]
                    if self.price == 0:
                        print("Seat is already taken, please select another seat")
                    else:
                        break
                except:
                    print('Invalid choice, try again')
                    
            print(f"\nYour selected booking details are as follows:\nservice: {self.service}\nselected seat: {self.seat}\nselected date: {self.date}\nselected timeslot: {self.time}\nSeat Price: {self.price}")
            ans = str(input("\nType yes to confirm seat booking or no to reselect\n"))
            if ans=='yes':
                print("\nSeat Booking Confirmed")
                available_rooms[owner_index][self.service]["price_for_each_seat"][index][row-1,col-1] = 0
                if self.name not in booking_track[owner_index][self.service]:
                    booking_track[owner_index][self.service][self.name]=[]
                booking_track[owner_index][self.service][self.name].append(str(self.price)+'_'+str(self.date)+'_'+str(self.time)+'_'+str(row)+'-'+str(col))
                print(booking_track)
                return available_rooms,booking_track,sell_list
            else:
                continue
        
        #self.booked_seat = seat 
    
    def change_booking(self, new_seat):
        self.booked_seat = new_seat
    
    def cancel_booking(self):
        self.booked_seat = None
    
    def sell_seat(self, seat, sell_list):
        sell_list.add_seat(seat)
    
    def send_complaint(self, complaint, admin):
        admin.receive_complaint(complaint)

class Admin:
    def __init__(self):
        pass
    #     self.user = user
    def view_bookings(self):
        print(booking_track)
    def modify_bookings(self):
        for i in a : print(i,end="\n")
        modify_user=input("Please select a user to modify his/her bookings \n")
        # view_Modify_user=[]
        if modify_user in str(booking_track):
            for owner_key in booking_track:
                for business in booking_track[owner_key]:
                    for User in booking_track[owner_key][business]:
                        if User == modify_user:
                            booking_details = booking_track[owner_key][business][User][0]
                            booked_seat = booking_details.split('_')[3]
                            booked_date = booking_details.split('_')[1]
                            booked_time = booking_details.split('_')[2]
                            booked_price = booking_details.split('_')[0]
                            booked_row = booked_seat.split('-')[0]
                            booked_column = booked_seat.split('-')[1]
                            print(f"Owner_key is {owner_key} business is {business}")
                            print(f"Below are the Current Booking details,Please reselct booking  \n Booked Seat:{booked_seat} \n Booked Price:{booked_price} \n Booked Date:{booked_date} \n Booked_Time:{booked_time} \n Booked Row:{booked_row} \n Booked_column:{booked_column}")
                            u=user(modify_user)
                            for i in range(len(available_rooms[owner_key][business]['dates'])):
                                if booked_date == available_rooms[owner_key][business]['dates'][i]:
                                    selected_option_date = i
                            for i in range(len(available_rooms[owner_key][business]['times'])):
                                if booked_time == available_rooms[owner_key][business]['times'][i]:
                                    selected_option_time = i
                            index = selected_option_date*selected_option_time-1
                            #print(available_rooms[owner_key][business]['price_for_each_seat'][index][int(booked_row)-1][int(booked_column)-1])   #Price before update
                            available_rooms[owner_key][business]['price_for_each_seat'][index][int(booked_row)-1][int(booked_column)-1] = booked_price
                            #print(available_rooms[owner_key][business]['price_for_each_seat'][index][int(booked_row)-1][int(booked_column)-1])   #Price after update
                            booking_track[owner_key][business][User]=[]
                            u.book_seat(available_rooms)
                            
        else:
            print("This User has no Bookings , Please select another User \n")
            adm.modify_bookings()
    def view_business(self):
        print(available_rooms)

    
def authenticate():
    global users, owners, admin
    while True:
        while True:
            username = str(input("Username: "))
            if username in users or username in owners or username in admin:
                password = gp.getpass(prompt = 'Enter the password')
                #password = str(input("Password: ")); 
            else: print("\nUser does not exist, Try again! \n"); 

            if username in users: 
                if users[username]==password: print("\nAuthentication Successful, Logging in"); role = "user_"+username; return role
                else: print("Incorrect password, try again")
            elif username in owners:
                if owners[username]==password: print("\nAuthentication Successful, Logging in"); role = "owner_"+username; return role
                else: print("Incorrect password, try again")
            elif username in admin: 
                if admin[username]==password: print(("\nAuthentication Successful, Logging in")); role = "admin_"+username; return role
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
            
        
def  Complaintbox(user,role):
    if role == "admin":
        for key,value in complaints.items():
            print(key,value)
    else:
        complaint=input("Please tell me your concern so I can report it to the developers: \n")
        complaints[user]=complaint
            
def msg_all(msg,current_user):
    for user in all_users:
        if(current_user != user):
            message_dict[user].append(msg)

if __name__ == '__main__':
    available_rooms ={}
    booking_track={}
    sell_list ={}

    while True:
        print("Hello, Welcome to our seat booking application!\n")
        print("Please enter your login credentials")
        role = authenticate()
        name = role.split('_')[1]
        print(f"Welcome {name}!")

        if role.split('_')[0] == 'owner':

            if name not in available_rooms:
                available_rooms[name]={}
                booking_track[name]={}
                service, size, reg_price = get_owner_details()
                available_rooms[name][service]={}
                booking_track[name][service]={}
                available_rooms[name][service]['price_for_each_seat']= [];available_rooms[name][service]['dates'] =[]; available_rooms[name][service]['times']=[]; #available_rooms[name]['messages'] =[]
                #messages=[]
            else:
                print('\n your existing room details are as follows: ')
                print("\n", available_rooms[name])
                ans = str(input("\n If you want to add another room, press yes otherwise press q to exit: "))
                if ans == 'q':
                    continue
                if ans=='yes':
                    while True:
                        service, size, reg_price = get_owner_details()
                        if service not in available_rooms[name]:
                            available_rooms[name][service]={}
                            booking_track[name]={}
                            available_rooms[name][service]['price_for_each_seat']= [];available_rooms[name][service]['dates'] =[]; available_rooms[name][service]['times']=[]; #available_rooms[name]['messages'] =[]
                            break
                        else:
                            print("Service already exists, try again!")

            o = owner(service, size, reg_price)

            while True:
                #if service not in available_rooms[name].keys():
                #    available_rooms[name][service]={}
                #    available_rooms[name][service]['price_for_each_seat']= [];available_rooms[name][service]['dates'] =[]; available_rooms[name][service]['times']=[]; #available_rooms[name]['messages'] =[]

                available_rooms[name][service]['dates']=o.select_dates()
                available_rooms[name][service]['times']=o.select_times()
                for i in range(len(available_rooms[name][service]['dates'])*len(available_rooms[name][service]['times'])):
                    available_rooms[name][service]['price_for_each_seat'].append(o.set_price())
                #available_rooms[name]['messages'].append(o.get_messages())
                print("\n Your details are saved: \n")
                ans = str(input("\n If you want to add another room, enter yes \n if you want to view existing rooms, enter show\n otherwise press q to exit"))
                if ans == 'show':
                    print(available_rooms[name])
                    ans = str(input("\n If you want to add another room, enter yes \n otherwise press q to exit: "))
                if ans=='yes':
                    while True:
                        service, size, reg_price = get_owner_details()
                        if service not in available_rooms[name]:
                            available_rooms[name][service]={}
                            booking_track[name]={}
                            available_rooms[name][service]['price_for_each_seat']= [];available_rooms[name][service]['dates'] =[]; available_rooms[name][service]['times']=[]; #available_rooms[name]['messages'] =[]
                            break
                        else:
                            print("Service already exists, try again!")
                if ans=='q':
                    break
                continue

        if role.split('_')[0] == 'user':
            u = user(name)
            while True:
                available_rooms, booking_track, sell_list = u.get_action(available_rooms, booking_track, sell_list)
                ans = str(input("\n If you want to go back, enter b \n otherwise press q to exit: "))
                if ans == 'b':
                    continue
                else:
                    break
        if role.split('_')[0] == 'admin':
            adm=Admin()
            while True:
                admin_tasks  = ['View Bookings','Modify Bookings','View Business','View Complaints']
                for i, task in enumerate(admin_tasks):
                    print(f"{i+1}. {task}")
                activity = int(input("\n Please Select a option\n"))
            
                if activity == 1:
                    adm.view_bookings()
                    ans = str(input("\n If you want to go back, enter b \n otherwise press q to exit: "))
                    if ans == 'b':
                        continue
                    else:
                        break
                elif activity == 2:
                    adm.modify_bookings()
                    ans = str(input("\n If you want to go back, enter b \n otherwise press q to exit: "))
                    if ans == 'b':
                        continue
                    else:
                        break
                elif activity == 3:
                    adm.view_business()
                    ans = str(input("\n If you want to go back, enter b \n otherwise press q to exit: "))
                    if ans == 'b':
                        continue
                    else:
                        break
                
                elif activity == 4:
                    Complaintbox(role.split('_')[1], role.split('_')[0])
                    ans = str(input("\n If you want to go back, enter b \n otherwise press q to exit: "))
                    if ans == 'b':
                        continue
                    else:
                        break            
        continue


#sell list (resell)
#cancel 
