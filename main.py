import math
import numpy as np
import getpass as gp
import copy

users = {"Gargee":"123", "Akshay":"456", "prof":"789"}
owners = {"owner1": "abc", "owner2":"xyz", "owner3":"efg"}
admin = {"admin": "123"}

message_dict ={}
complaints={}
a = list(users.keys()); b = list(owners.keys()); c = list(admin.keys())
all_users=a+b+c

for i in range(len(all_users)):
    temp_user_list = all_users.copy() #i=Gargee
    temp_user_list.pop(i)
    message_dict[all_users[i]]={}
    for j in range(len(temp_user_list)): #j=prof
        message_dict[all_users[i]][temp_user_list[j]]=[]

for i in all_users:
    complaints[i]=''

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
                selected_opt = set(map(int, input("\nEnter your choices (separated by spaces): ").split()))
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
                selected_opt = set(map(int, input("\nEnter your choices (separated by spaces): ").split()))
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
    
    def get_action(self, available_rooms,booking_track,sell_list,sl_watchers):
        options=['New Reservation', 'Existing Reservation', 'Messaging Service','Visit Sell List']
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
            a,b,s = u.book_seat(available_rooms,booking_track)
            return a,b,s,sl_watchers
        
        if choice==2:
            if not booking_track:
                    print("No Reservations")
            else:
                count=0
                for id in booking_track:
                    for serv in booking_track[id]:
                        if self.name in booking_track[id][serv]:
                            count+=1
                if count==0:
                    print("You have no reservations")
                    return available_rooms,booking_track,sell_list,sl_watchers


            options = ['View','Cancel Ticket', 'Sell Ticket','Exchange Ticket']
            print("\nPlease select:")
            for i, option in enumerate(options):
                print(f"{i+1}. {option}")
            while True:
                try:
                    selected_option = int(input("\nEnter your choice: "))
                    if selected_option>len(options) or selected_option<0 or type(selected_option) is not int:
                        print('\nInvalid choice, try again')
                    else:
                        break
                except:
                    print('\nInvalid choice, try again')
            choice = options[selected_option-1]

            if selected_option==1: 
                if not booking_track:
                    print("\nNo Reservations")
                else:
                    for id in booking_track:
                        for serv in booking_track[id]:
                            if self.name in booking_track[id][serv]:
                                for i in range(len(booking_track[id][serv][self.name])):
                                    details = booking_track[id][serv][self.name][i].split('_')
                                    print(f"\nService: {serv}\nPrice: {details[0]}\nDate: {details[1]}\nTime: {details[2]}\nSeat row col: {details[3]}")
                            else:
                                continue
                return available_rooms,booking_track,sell_list,sl_watchers


            if selected_option == 2: 
                available_rooms, booking_track = u.cancel_booking(available_rooms,booking_track)
                return available_rooms,booking_track,sell_list,sl_watchers

            if selected_option == 3: 
                sell_list = u.sell_seat(booking_track, sell_list, sl_watchers)
                return available_rooms,booking_track,sell_list,sl_watchers



            if choice==4: u.exchange_booking

        if(choice == 3):
            message(self.name)
            return available_rooms,booking_track,sell_list,sl_watchers
        
        if(choice==4):
            sl_watchers.append(self.name)
            print("\nYour name has been added to sell list watchers as you visited the sell list\n")
            if sell_list:
                for key,value in sell_list.items():
                    print(key)
                    for i in value:
                        details=i.split("_")
                        print(f"\nService: {details[0]}\nSeat Number (row-col): {details[4]}\nOriginal Price: {details[1]}\nDate: {details[2]}\nTime: {details[3]}\nDiscount Ratio: {details[-1]}\n")
            else:
                print("\nSell list is empty")
            
            ans=str(input("\nIf you wish to buy from sell_list, please message the respective person.\nTo go to messaging service press m else press any other key to go back"))
            if ans=='m':
                message(self.name)
                return available_rooms,booking_track,sell_list,sl_watchers
            else:
                return available_rooms,booking_track,sell_list,sl_watchers

        
    
    def sell_seat(self,booking_track, sell_list,sl_watchers):
        service=[]
        bookings=[]
        print("\nEnter the booking that you want to sell:\n")
        for id in booking_track:
            for serv in booking_track[id]:
                if self.name in booking_track[id][serv]:
                    service.append(serv)
                             
        print("\n Enter service numbers to be sold: ")
        for a, option in enumerate(service):
            print(f"{a+1}. {option}")
        while True:
            try:
                selected_option = int(input("\nEnter your choice: "))
                if selected_option>len(service) or selected_option<0:
                    print('\nInvalid choice, try again')
                else:
                    break
            except:
                print('\nInvalid choice, try again')
        serv_to_sell = service[selected_option-1]

        for id in booking_track:
            if serv_to_sell in booking_track[id]:
                for i in booking_track[id][serv_to_sell][self.name]:
                    bookings.append(i)

        print("\n Enter booking to be sold: ")
        for a, option in enumerate(bookings):
            details=option.split("_")
            print(f"{a+1}. \nPrice: {details[0]}\nDate: {details[1]}\nTime: {details[2]}\nSeat Row-Column: {details[3]}")
        while True:
            try:
                selected_option = int(input("\nEnter your choice: "))
                if selected_option>len(service) or selected_option<0:
                    print('\nInvalid choice, try again')
                else:
                    break
            except:
                print('\nInvalid choice, try again')
            
        booking_to_sell = bookings[selected_option-1]

        while True:
            try:
                disc_ratio = int(input("\nEnter Discount Ratio in percentage: "))
                if disc_ratio<0 or disc_ratio>100:
                    print("\nInvalid Discount ratio, try again!")
                    continue
                else:
                    break
            except:
                print("Please choose an integer between 1 to 100, try again!")
                continue

        for id in booking_track:
            if serv_to_sell in booking_track[id]:
                if self.name not in sell_list:
                    sell_list[self.name]=[]
                sell_list[self.name].append(serv_to_sell+'_'+booking_track[id][serv_to_sell][self.name][selected_option-1]+'_'+str(disc_ratio))

        print("\n Booking added to Sell list, all sell list watchers will be notified!")
        print(sell_list)
        msg_all("Hey, I added a new Booking to Sell List that you are watching!",self.name, sl_watchers)
        return sell_list
    


    def book_seat(self, available_rooms, booking_track):
        while True:
            print("\nAvailable services: ")
            options=[]
            for i in available_rooms.keys():
                for key in available_rooms[i]:
                    options.append(i+"_"+key)
                
            
            while True:
                if len(options)==0: 
                    print("No services available\n")
                    return available_rooms,booking_track,sell_list
                else:
                    break
            
            for a, option in enumerate(options):
                id = option.split("_")[0]
                serv = option.split("_")[1]
                print(f"{a+1}. Direct Owner {id}: {serv}")
            '''
            if sell_list:
                for key,value in sell_list.items():
                    print(key)
                    for i in value:
                        details=i.split("_")
                        print(f"\nService: {details[0]}\n")
                        print("To buy from Sell List, visit sell_list")
                        
            else:
                print("\nSell list is empty")
                '''
            
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
            self.service = options[selected_option-1].split("_")[1]

            for i in available_rooms.keys():
                for key in available_rooms[i]:
                    if key==self.service:
                        owner_index = i
                        break
            
            print("\nSelect date from the available date list\n")
            options_dates = available_rooms[owner_index][self.service]["dates"]
            for a, option in enumerate(options_dates):
                print(f"{a+1}. {option}")
            while True:
                try:
                    selected_option_date = int(input("\nEnter your choice: "))
                    if selected_option_date>len(options_dates) or selected_option_date<0:
                        print('\nInvalid choice, try again')
                    else:
                        break
                except:
                    continue
            self.date = options_dates[selected_option_date-1]

            print("\nSelect time from the available time list\n")
            options_times = available_rooms[owner_index][self.service]["times"]
            for a, option in enumerate(options_times):
                print(f"{a+1}. {option}")
            while True:
                try:
                    selected_option_time = int(input("\nEnter your choice: "))
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
                                    print(f"You already have a reservation in this time slot for {serv}, please try again or press q to exit")
                                    red_flag = 1
            
            if red_flag==1:
                return available_rooms,booking_track,sell_list
            
            index = selected_option_date*selected_option_time-1
            while True:
                try:
                    print("Seat Layout with price for each seat (displayed top row is the 1st front row): \n")
                    print(available_rooms[owner_index][self.service]["price_for_each_seat"][index])
                    print("Seats marked 0 are unavailable for booking")
                    while True:
                        self.seat = str(input("\nSelect row,column desired seat (Separated by space): "))
                        row, col = int(self.seat.split(" ")[0]), int(self.seat.split(" ")[1])
                        check_shape= available_rooms[owner_index][self.service]["price_for_each_seat"][index].shape[0]
                        if row>check_shape or col>check_shape or row<=0 or col<=0:
                            print("Invalid seat choice, please try again")
                        else: break
                    self.price = available_rooms[owner_index][self.service]["price_for_each_seat"][index][row-1,col-1]
                    if self.price == 0:
                        print("Seat is already taken, please select another seat")
                    else: break
                except: print('Invalid choice, try again')
                    
            print(f"\nYour selected booking details are as follows:\nservice: {self.service}\nselected seat: {self.seat}\nselected date: {self.date}\nselected timeslot: {self.time}\nSeat Price: {self.price}")
            ans = str(input("\nType yes to confirm seat booking or no to reselect\n"))
            if ans=='yes':
                print("\nSeat Booking Confirmed")
                available_rooms[owner_index][self.service]["price_for_each_seat"][index][row-1,col-1] = 0
                if self.name not in booking_track[owner_index][self.service]:
                    booking_track[owner_index][self.service][self.name]=[]
                booking_track[owner_index][self.service][self.name].append(str(self.price)+'_'+str(self.date)+'_'+str(self.time)+'_'+str(row)+'-'+str(col)+'_'+str(index))
                print(booking_track)
                return available_rooms,booking_track,sell_list
            else:
                continue
    
    def change_booking(self, new_seat):
        self.booked_seat = new_seat
    
    def cancel_booking(self, available_rooms, booking_track):
        service=[]
        bookings=[]
        print("\nPlease note that cancellation will lead to no refund so you will loose all money or you can explore the sell option\n")
        ans = str(input("\nPress q to quit or anyother key to continue\n"))
        if ans=='q':
            return available_rooms,booking_track

        print("\nEnter the service whose booking you want to delete:\n")
        for id in booking_track:
            for serv in booking_track[id]:
                if self.name in booking_track[id][serv]:
                    service.append(serv)
                             
        print("\n Enter service numbers to be deleted: ")
        for a, option in enumerate(service):
            print(f"{a+1}. {option}")
        while True:
            try:
                selected_option = int(input("\nEnter your choice: "))
                if selected_option>len(service) or selected_option<0:
                    print('\nInvalid choice, try again')
                else:
                    break
            except:
                print('\nInvalid choice, try again')
        serv_to_del = service[selected_option-1]

        for id in booking_track:
            if serv_to_del in booking_track[id]:
                for i in booking_track[id][serv_to_del][self.name]:
                    bookings.append(i)

        print("\n Enter booking to be deleted: ")
        for a, option in enumerate(bookings):
            details=option.split("_")
            print(f"{a+1}. \nPrice: {details[0]}\nDate: {details[1]}\nTime: {details[2]}\nSeat Row-Column: {details[3]}")
        while True:
            try:
                selected_option = int(input("\nEnter your choice: "))
                if selected_option>len(service) or selected_option<0:
                    print('\nInvalid choice, try again')
                else:
                    break
            except:
                print('\nInvalid choice, try again')
            
        booking_to_del = bookings[selected_option-1]
        index = int(booking_to_del.split('_')[-1])
        row= int((booking_to_del.split('_')[-2]).split('-')[0])
        col= int((booking_to_del.split('_')[-2]).split('-')[1])
        price = float(booking_to_del.split('_')[0])
       
        for id in booking_track:
            if serv_to_del in booking_track[id]:
                del booking_track[id][serv_to_del][self.name][selected_option-1]

                available_rooms[id][serv_to_del]["price_for_each_seat"][index][row-1,col-1] = price

        print("\n Booking Successfully Cancelled without any refund")

        return available_rooms,booking_track

    
    def send_complaint(self, complaint, admin):
        admin.receive_complaint(complaint)


    
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
                else: print("\nIncorrect password, try again")
            elif username in owners:
                if owners[username]==password: print("\nAuthentication Successful, Logging in"); role = "owner_"+username; return role
                else: print("\nIncorrect password, try again")
            elif username in admin: 
                if admin[username]==password: print(("\nAuthentication Successful, Logging in")); role = "admin"; return role
                else: print("\nIncorrect password, try again")

def message(Current_User):
    msg_service = ['Check Messages','Send a message to user']
    print("\nPlease Select an option:")
    j=1
    for i in msg_service:
        print(j,": " ,i)
        j+=1
    opt=int(input())
    if opt == 1:
        print("\nMessages for ",Current_User,"\n")
        for i in message_dict[Current_User]:
            print(i,":") 
            inner_dict = message_dict[Current_User]
            #print("inner_dict ",inner_dict)
            message_list=inner_dict[i]
            #print("message_list ",message_list)
            for msg in message_list:
                print(msg)
            print()
        
                
    elif opt == 2:
        while True:
            print("\nSelect a User to send Message or press q to exit")
            for x in range(len(all_users)):
                if all_users[x] != Current_User:print(all_users[x])
            req_user = input()
            if req_user in all_users:
                print("\nplease type in a message to send to ",req_user)
                message=input()
                message_dict[req_user][Current_User].append(message)
                print(f"\nMessage Sent Successfully to {req_user}!")
                break
            elif req_user == 'q':
                break
            else:
                print("\nInvalid user entered, Try again!\n")
                continue
        
            
def msg_all(msg,current_user,pool):
    for user in pool:
        if(current_user != user):
            message_dict[user][current_user].append(msg)
            
def  Complaintbox(user,role):
    if role == "admin":
        for key,value in complaints.items():
            print(key,value)
    else:
        complaint=input("\nPlease tell me your concern so I can report it to the developers: \n")
        complaints[user]=complaint


if __name__ == '__main__':
    available_rooms ={}
    booking_track={}
    sell_list ={}
    sl_watchers=[]

    while True:
        print("\nHello, Welcome to our seat booking application!\n")
        print("\nPlease enter your login credentials")
        role = authenticate()
        name = role.split('_')[1]
        print(f"\nWelcome {name}!")

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
                ans = str(input("\n If you want to add another room, press yes otherwise press any other key to exit: "))
                if ans=='yes':
                    while True:
                        service, size, reg_price = get_owner_details()
                        if service not in available_rooms[name]:
                            available_rooms[name][service]={}
                            booking_track[name][service]={}
                            available_rooms[name][service]['price_for_each_seat']= [];available_rooms[name][service]['dates'] =[]; available_rooms[name][service]['times']=[]; #available_rooms[name]['messages'] =[]
                            break
                        else:
                            print("\nService already exists, try again!")
                else:
                    print("\nInvalid response, exitting!")
                    continue

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
                elif ans=='yes':
                    while True:
                        service, size, reg_price = get_owner_details()
                        if service not in available_rooms[name]:
                            available_rooms[name][service]={}
                            booking_track[name][service]={}
                            available_rooms[name][service]['price_for_each_seat']= [];available_rooms[name][service]['dates'] =[]; available_rooms[name][service]['times']=[]; #available_rooms[name]['messages'] =[]
                            break
                        else:
                            print("\nService already exists, try again!")
                            continue
                else:
                    print("\nYou either pressed q or invalid key, exitting")
                    break

        if role.split('_')[0] == 'user':
            u = user(name)
            while True:
                print(booking_track)
                available_rooms, booking_track, sell_list,sl_watchers = u.get_action(available_rooms, booking_track, sell_list,sl_watchers)
                ans = str(input("\n If you want to go back, enter b \n otherwise press q to exit: "))
                if ans == 'b':
                    continue
                else:
                    break
        continue

'''
To do
exchange booking (simple chatting) (exchange agreed, send request for ticket transfer if both parties accept, exchange and modify booking_track)
modify book_seat, 1. New Reservation > Buy from direct owner or reseller, if reseller modify accounding based on sell_list (resell and point 4)
Integrate Akshay's code 
'user'_admin
remove unnecessary print dicts at the end

solved
keyerror for when owner adds 2 services
cancel booking
error handling
view sell_list
add to sell_list
notify sell_list watchers (message_all)
Integrated 2 way messaging, msg_all and complaint functions
'''
