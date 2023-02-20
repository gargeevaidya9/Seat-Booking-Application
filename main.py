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

available_rooms ={}
booking_track={}
sell_list ={}
sl_watchers=[]

confirm_resell={}
confirm_exchange={}

for i in range(len(all_users)):
    temp_user_list = all_users.copy() #i=Gargee
    temp_user_list.pop(i)
    message_dict[all_users[i]]={}
    for j in range(len(temp_user_list)): #j=prof
        message_dict[all_users[i]][temp_user_list[j]]=[]


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
                print("\nPlease select dates:")
                options = ["1/1/23", "2/1/23", "3/1/23", "4/1/23"]
                for i, option in enumerate(options):
                    print(f"{i+1}. {option}")
                selected_opt = set(map(int, input("\nEnter your choices (separated by spaces): ").split()))
                selected_options = [options[i-1] for i in selected_opt if i > 0 and i <= len(options)]
                for i in selected_opt:
                    if int(i)>len(options) or int(i)<0:
                        print("\nInvalid choice try again")
                    else:
                        return selected_options
            except:
                print("\nPlease enter an integer value")

    def select_times(self):
        while True:
            try:
                print("\nPlease select times:")
                options = ["18:00", "19:00", "20:00", "21:00"]
                for i, option in enumerate(options):
                    print(f"{i+1}. {option}")
                selected_opt = set(map(int, input("\nEnter your choices (separated by spaces): ").split()))
                selected_options = [options[i-1] for i in selected_opt if i > 0 and i <= len(options)]
                for i in selected_opt:
                    if int(i)>len(options) or int(i)<0:
                        print("\nInvalid choice try again")
                    else:
                        return selected_options
            except:
                print("\nPlease enter an integer value")
    
def get_owner_details():

    while True:
        try:
            service=str(input("\nEnter Service: "))
            if len(service)<1 or len(service)>100:
                print("\nService name must be minimum 1 character and maximum 100 characters, Try again!")
                continue
            else:
                break
        except:
            print("\nInvalid service name entered, please Trye again!")

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
            a,b,s = u.book_seat(available_rooms,booking_track, sell_list)
            return a,b,s,sl_watchers
        
        if choice==2:
            if not booking_track:
                    print("No Reservations")
                    return available_rooms,booking_track,sell_list,sl_watchers
            else:
                count=0
                flag=' '
                for id in booking_track:
                    for serv in booking_track[id]:
                        if self.name in booking_track[id][serv]:
                            count+=1
                            if len(booking_track[id][serv][self.name])==0:
                                flag='set'
                if count==0 or flag=='set':
                    print("You have no reservations")
                    return available_rooms,booking_track,sell_list,sl_watchers


            options = ['View','Cancel Ticket', 'Sell Ticket','Exchange Ticket','Change Ticket']
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
                    check=0
                    for id in booking_track:
                        for serv in booking_track[id]:
                            if self.name in booking_track[id][serv]:
                                check+=1
                                for i in range(len(booking_track[id][serv][self.name])):
                                    details = booking_track[id][serv][self.name][i].split('_')
                                    print(f"\nService: {serv}\nPrice: {details[0]}\nDate: {details[1]}\nTime: {details[2]}\nSeat row col: {details[3]}")
                            else:
                                continue
                    if check==0:
                        print("\nNo Reservations")
                return available_rooms,booking_track,sell_list,sl_watchers


            if selected_option == 2: 
                available_rooms, booking_track = u.cancel_booking(available_rooms,booking_track)
                return available_rooms,booking_track,sell_list,sl_watchers

            if selected_option == 3: 
                sell_list = u.sell_seat(booking_track, sell_list, sl_watchers)
                return available_rooms,booking_track,sell_list,sl_watchers

            if selected_option==4: 
                u.exchange_booking()
                return available_rooms,booking_track,sell_list,sl_watchers

            if selected_option==5: 
                u.change_booking()
                return available_rooms,booking_track,sell_list,sl_watchers

        if(choice == 3):
            booking_track = message(self.name,booking_track)
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
                ans=str(input("\nIf you wish to buy from sell_list, please message the respective person.\nTo go to messaging service press 'dm' else press any other key to go back"))
                if ans=='dm':
                    booking_track=message(self.name,booking_track)
                    return available_rooms,booking_track,sell_list,sl_watchers
                else:
                    return available_rooms,booking_track,sell_list,sl_watchers
            else:
                print("\nSell list is empty")
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
                else:
                    for i in sell_list[self.name]:
                        if i == (serv_to_sell+'_'+booking_track[id][serv_to_sell][self.name][selected_option-1]+'_'+str(disc_ratio)):
                            print("\nBooking already exists in Sell list")
                            return sell_list
                        
                sell_list[self.name].append(serv_to_sell+'_'+booking_track[id][serv_to_sell][self.name][selected_option-1]+'_'+str(disc_ratio))

        print("\n Booking added to Sell list, all sell list watchers will be notified!")
        
        msg_all("Hey, I added a new Booking to Sell List that you are watching!",self.name, sl_watchers)
        return sell_list
    


    def book_seat(self, available_rooms, booking_track, sell_list):
        while True:
            print("\nAvailable services: ")
            options=[]
            for i in available_rooms.keys():
                for key in available_rooms[i]:
                    options.append(i+"_"+key)
                
            
            while True:
                if len(options)==0: 
                    print("\nNo services available\n")
                    return available_rooms,booking_track,sell_list
                else:
                    break
            print("\nBuy from Direct Owners")
            for a, option in enumerate(options):
                id = option.split("_")[0]
                serv = option.split("_")[1]
                print(f"{a+1}. Direct Owner {id}: {serv}")
            

            if sell_list:
                print("\nBuy from Resellers:")
                for key,value in sell_list.items():
                    if key!=self.name:
                        for i in value:
                            details=i.split("_")
                            print(f"Reseller {key}: {details[0]}\n")
                        
            else:
                print("\nSell list is empty")
            
            while True:
                
                if sell_list:
                    check = str(input("\nTo buy from a Reseller, please press 'b' or press any other key to continue booking from direct owners: "))
                    if check=='b':
                        u.buy_from_sell_list(sell_list,booking_track)
                        return available_rooms,booking_track,sell_list
                    else:
                        break
                else:
                    break   
                #except:
                #    print('\nInvalid choice, try again')

            while True:
                try:
                    selected_option = int(input("\nselect service: "))
                    if selected_option>len(options) or selected_option<0 or type(selected_option) is not int:
                        print('\nInvalid choice, try again')
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
            while True:
                try:
                    ans = str(input("\nType yes to confirm seat booking or no to reselect\n"))
                    if ans in ['yes','no']:
                        break
                    else:
                        print("\nInvalid Input, Try again!")
                        continue
                except:
                    continue
            if ans=='yes':
                print("\nSeat Booking Confirmed")
                available_rooms[owner_index][self.service]["price_for_each_seat"][index][row-1,col-1] = 0
                if self.name not in booking_track[owner_index][self.service]:
                    booking_track[owner_index][self.service][self.name]=[]
                booking_track[owner_index][self.service][self.name].append(str(self.price)+'_'+str(self.date)+'_'+str(self.time)+'_'+str(row)+'-'+str(col)+'_'+str(index))
                
                return available_rooms,booking_track,sell_list
            else:
                continue
    
    def buy_from_sell_list(self,sell_list,booking_track):
        if sell_list:
            for key,value in sell_list.items():
                if key != self.name:
                    for i in value:
                        details=i.split("_")
                        print(f"\nReseller {key}: {details[0]}\n")            
        else:
            print("\nSell list is empty")

        ans = str(input("\nTo buy a ticket from reseller, please send a direct message\n To send a direct message press 'dm' else press any other key to go back: "))
        if ans =='dm':
            booking_track=message(self.name,booking_track)

    def exchange_booking(self):
        if self.name in sell_list:
            print("\nYou have a booking in sell_list so you are elligible to exchange your ticket with someone else from the sell_list\nAvailable bookings in sell list that you can exchange with are:\n")
            flag=0
            for key,value in sell_list.items():
                if key!=self.name:
                    flag+=1
                    for count,i in enumerate(value):
                        print(key)
                        details=i.split("_")
                        print(f"\nService: {details[0]}\nSeat Number (row-col): {details[4]}\nOriginal Price: {details[1]}\nDate: {details[2]}\nTime: {details[3]}\nDiscount Ratio: {details[-1]}\n")
            if flag==0:
                print("\nNo other booking available in sell list that you can exchange with!")

            ans = str(input("\nPress any key to continue the exchange process, or press 'q' quit\n"))
            if ans=='q':
                return
            else:
                print("\nDirecting you to messaging service where you can send a message to the person you wish to exchange your booking with,\nif they agree in chat, you can go to messaging service>confirm exchange service where exchange will be completed once both parties acceptt the deal!\n")
                message(self.name,booking_track)
                
        else:
            print("\nYou are not elligible to exchange ticket as none of your bookings are in the sell_list!\n")
            return
    
    def change_booking(self):
        print("\nPlease note that changing your booking will lead to no refund and you will be charged fully for the new_booking,\n or you can explore the sell or exchange option\n")
        ans = str(input("\nPress q to quit or anyother key to continue\n"))
        if ans=='q':
            return
        else:
            print("\nIf you still wish to change your booking, please go to Cancel Booking and then go to New reservation!\n")
            return
    
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

class Admin:
    def __init__(self):
        pass
    #     self.user = user
    def view_bookings(self):
        print(booking_track)
    def modify_bookings(self):
        for i in a : print(i,end="\n")
        while True:
            modify_user=input("Please select a user to modify his/her bookings \n")
            if modify_user in all_users: break
            else: print("\nInavlid user, try again!")

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
                            print(f"Owner is {owner_key} Service is {business}")
                            print(f"Below are the Current Booking details\n Booked Seat:{booked_seat} \n Booked Price:{booked_price} \n Booked Date:{booked_date} \n Booked_Time:{booked_time} \n Booked Row:{booked_row} \n Booked_column:{booked_column}")
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
                            while True:
                                try:
                                    ans = str(input(f"\nBookings for {modify_user} deleted, Do you want to do new booking on {modify_user}'s behalf? (yes/no) "))
                                    if ans in ['yes','no']:
                                        if ans=='yes':
                                            u.book_seat(available_rooms,booking_track,sell_list)
                                        else:
                                            return
                                    else: print("\nInvalid response, try again!")
                                except:
                                    print("\nInvalid response, try again!")
                            
        else:
            ans = input("This User has no Bookings , Please select another User or press q to quit\n")
            if ans=='q':
                return
            else: adm.modify_bookings()

    def view_business(self):
        print(available_rooms)
    
    def view_sell_list(self):
        print(sell_list)
    
    def view_confirm_exchange_requests(self):
        print(confirm_exchange)

    def view_confirm_resell_requests(self):
        print(confirm_resell)
    
    def view_sell_list_watchers(self):
        print(sl_watchers)


    
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

def message(Current_User, booking_track):
    global confirm_resell
    global confirm_exchange

    if Current_User in list(users.keys()):
       all_users = list(users.keys())+list(admin.keys()) 
    elif Current_User in list(owners.keys()):
       all_users = ['admin']
    else:
        all_users = list(users.keys())+list(admin.keys())+list(owners.keys())

    if Current_User == 'admin':    
        while True:
            print("\nAvailable users to chat with")
            for x in range(len(all_users)):
                if all_users[x] != Current_User:print(all_users[x])
            req_user = input("\nSelect a User to send Message or press q to exit: ")
            if req_user in all_users:
                print("\nPlease type in a message to send to: ",req_user)
                message=input()
                message_dict[req_user][Current_User].append(message)
                print(f"\nMessage Sent Successfully to {req_user}!")
                return booking_track
            elif req_user == 'q':
                return booking_track
            else:
                print("\nInvalid user entered, Try again!\n")
                continue  
 
    if Current_User in list(owners.keys()):
        msg_service = ['Check Messages','Send a message to user']
    else:
        msg_service = ['Check Messages','Send a message to user','Confirm Resell','Confirm Exchange']

    j=1
    for i in msg_service:
        print(j,": " ,i)
        j+=1
    
    while True:
        try:
            opt=int(input("\nPlease Select an option:"))
            if not (opt>len(msg_service) or opt<0):
                break
            else:
                print("\nInvalid choice, Try again!\n")
                continue
        except:
            print("\nInvalid choice, Try again!\n")
            continue

    if opt==1:
        count=0
        print("\nMessages for ",Current_User,"\n")
        for i in message_dict[Current_User]:
            inner_dict = message_dict[Current_User]
            #print("inner_dict ",inner_dict)
            message_list=inner_dict[i]
            #print("message_list ",message_list)
            if len(message_list)!=0: 
                count+=1
                print(i,":")     
                for msg in message_list:
                    print(msg)
                print()
        if count==0:
            print("\nNo Messages")

        return booking_track
                
    elif opt == 2:
        while True:
            print("\nAvailable users to chat with")
            for x in range(len(all_users)):
                if all_users[x] != Current_User:print(all_users[x])
            req_user = input("\nSelect a User to send Message or press q to exit: ")
            if req_user in all_users:
                print("\nPlease type in a message to send to: ",req_user)
                message=input()
                message_dict[req_user][Current_User].append(message)
                print(f"\nMessage Sent Successfully to {req_user}!")
                return booking_track
            elif req_user == 'q':
                return booking_track
            else:
                print("\nInvalid user entered, Try again!\n")
                continue
    elif opt==3:
        while True:
            ans = str(input("\nHave you confirmed a resell via chat with a user? (yes/no): "))
            if ans in ['yes','no']:
                if ans=='yes':
                    who = str(input("\nAre you the seller or buyer? (seller/buyer)"))
                    if who in ['seller','buyer']:
                        break
                    else:
                        print("\nInvalid choice, please try again!")
                        continue
                elif ans == 'no':
                    print("\nPlease confirm a resell with a user via chat and then visit this option to complete the resale!")
                    who=' '
                    break
            else:
                print("\nInvalid choice, please try again!")
                continue

        if who=='seller':
            while True:
                req_user = str(input("\nPlease enter the name of the user you agreed to sell the ticket to or press 'q' to exit: "))
                if req_user in all_users:
                    if Current_User in confirm_resell:
                        if req_user in confirm_resell[Current_User]:
                            if confirm_resell[Current_User][req_user].value == 'no':
                                print(f"\nResell not completed, {req_user} rejected the deal!\n")
                                print("\nYour confirm resell request will now be deleted!")
                                confirm_resell={}
                                return booking_track

                    else: confirm_resell[Current_User]={}

                    sell_options=[]
                    if sell_list:
                        for key,value in sell_list.items():
                            if key!=Current_User:
                                continue
                            else:
                                for count,i in enumerate(value):
                                    sell_options.append(i)
                                    print(f"{count+1}.")
                                    details=i.split("_")
                                    print(f"\nService: {details[0]}\nSeat Number (row-col): {details[4]}\nOriginal Price: {details[1]}\nDate: {details[2]}\nTime: {details[3]}\nDiscount Ratio: {details[-1]}\n")
                    else:
                        print("\nSell List is empty")
                        return booking_track

                    while True:
                        try:
                            selected_option = int(input("\nEnter your choice: "))
                            if selected_option>len(sell_options) or selected_option<0:
                                print('\nInvalid choice, try again')
                            else:
                                break
                        except:
                            print('\nInvalid choice, try again')

                    booking_to_sell = sell_options[selected_option-1]

                    if len(message_dict[Current_User][req_user])>=1: #Buyer has sent atleast 1 text message to seller
                        confirm_resell[Current_User][req_user]={booking_to_sell:''}
                        print("\nResell has been confirmed from your side, If buyer accepts, resell process will be completed\n")
                        return booking_track
                    else:
                        print(f"\nYou have no message history with {req_user}, you cannot resell to them, \nplease try again!")
                    continue

                elif req_user=='q':
                    return booking_track
                else:
                    print("\nInvalid user entered, Try again!\n")
                    continue                      
            
        
        if who=='buyer':
            while True:
                req_user = str(input("\nPlease enter the name of the user you agreed to buy the ticket from or press 'q' to exit: "))
                if req_user in all_users:
                    if req_user in confirm_resell:
                        if Current_User in confirm_resell[req_user]:                             
                            service = list(confirm_resell[req_user][Current_User].keys())[0]
                            print("\nDetails of the service to be sold are as follows:")
                            details=service.split("_")
                            print(f"\nService: {details[0]}\nSeat Number (row-col): {details[4]}\nOriginal Price: {details[1]}\nDate: {details[2]}\nTime: {details[3]}\nDiscount Ratio: {details[-1]}\n")
                            while True:
                                ans = str(input('Do you accept the resell deal? (yes/no)'))
                                if ans in ['yes','no']:
                                    break
                                else:
                                    print("\nInvalid choice. try again!")
                                    continue
                            if ans=='yes':
                                
                                for id in booking_track:
                                    if details[0] in booking_track[id]:
                                        if req_user in booking_track[id][details[0]]:
                                            for index,i in enumerate(booking_track[id][details[0]][req_user]):
                                                if i[:-2]==details[1]+'_'+details[2]+'_'+details[3]+'_'+details[4]:
                                                    del booking_track[id][details[0]][req_user][index]
                                                    for s_num,s in enumerate(sell_list[req_user]):
                                                        if s[2:-2]==i:
                                                            del sell_list[req_user][s_num]
                                                        if not sell_list[req_user]:
                                                            del sell_list[req_user]
                                                    if Current_User not in booking_track[id][details[0]]:
                                                        booking_track[id][details[0]][Current_User]=[]
                                                    booking_track[id][details[0]][Current_User].append(i)
                                                    print("\nResell Successfully Confirmed!")
                                                    confirm_resell={}
                                                    return booking_track
                            if ans=='no':
                                for service in confirm_resell[req_user][Current_User]:
                                    confirm_resell[req_user][Current_User][service]=='no'
                                    print("\nResell Request rejected!")
                                return booking_track

                        else:
                            print("\nSeller has not confirmed the deal, please wait for them to confirm the resell")
                            return booking_track
                    else:
                        print("\nSeller has not confirmed the deal, please wait for them to confirm the resell")
                        return booking_track
        
                elif req_user=='q':
                    return booking_track
                else:
                    print("\nInvalid user entered, Try again!\n")
                    continue 
        
    elif opt==4:
        if Current_User not in sell_list:
            print("You cannot exchange as none of your bookings are in sell_list")
            return booking_track

        while True:
            ans = str(input("\nHave you confirmed an exchange via chat with a user? (yes/no): "))
            if ans in ['yes','no']:
                if ans=='yes':
                    break
                elif ans == 'no':
                    print("\nPlease confirm an exchange with a user via chat and then visit this option to complete the exchange!")
                    break
            else:
                print("\nInvalid choice, please try again!")
                continue
            
        while True:
            req_user = str(input("\nPlease enter the name of the user you agreed to exchange the ticket with or press 'q' to exit: "))
            if req_user in all_users:
                break        
            elif req_user=='q':
                return booking_track
            else:
                print("\nInvalid user entered, Try again!\n")
                continue
        
        while True:
            exchange_options=[]
            print("\nSelect your booking from the sell_list that you wish to exchange:")
            for key,value in sell_list.items():
                if key!=Current_User:
                    continue
                else:
                    for count,i in enumerate(value):
                        exchange_options.append(i)
                        print(f"{count+1}.")
                        details=i.split("_")
                        print(f"Service: {details[0]}\nSeat Number (row-col): {details[4]}\nOriginal Price: {details[1]}\nDate: {details[2]}\nTime: {details[3]}\nDiscount Ratio: {details[-1]}\n")
            break


        while True:
            try:
                selected_option = int(input("\nEnter your choice: "))
                if selected_option>len(exchange_options) or selected_option<0:
                    print('\nInvalid choice, try again')
                else:
                    break
            except:
                print('\nInvalid choice, try again')
                continue

        booking_to_exchange = exchange_options[selected_option-1]
        

        if len(message_dict[Current_User][req_user])>=1 and len(message_dict[req_user][Current_User])>=1: #Both Exchangers have sent atleast 1 text message
            if req_user in confirm_exchange:
                if Current_User in confirm_exchange[req_user]:
                    service = list(confirm_exchange[req_user][Current_User].keys())[0]
                    print(f"\nDetails of the service that {req_user} wants to give you:")
                    details=service.split("_")
                    print(f"\nService: {details[0]}\nSeat Number (row-col): {details[4]}\nOriginal Price: {details[1]}\nDate: {details[2]}\nTime: {details[3]}\nDiscount Ratio: {details[-1]}\n")
                    while True:
                        ans = str(input('Do you accept the deal? (yes/no)'))
                        if ans in ['yes','no']:
                            if ans=='yes': 
                                confirm_exchange[req_user][Current_User]={service:'yes'}

                            else: confirm_exchange[req_user][Current_User]={service:'no'}
                            break
                        else:
                            print("\nInvalid choice. try again!")
                            continue

                    if Current_User not in confirm_exchange:
                        confirm_exchange[Current_User]={}

                    if req_user in confirm_exchange[Current_User]:
                        if list(confirm_exchange[Current_User][req_user].values())[0]=='yes' and ans=='yes':
                            print("\nBoth parties accepted, Exchange successfull")
                            service_cu = (list(confirm_exchange[Current_User][req_user].keys())[0]).split("_")[0]
                            service_ru = (list(confirm_exchange[req_user][Current_User].keys())[0]).split("_")[0]
                            for id in booking_track:
                                if service_cu in booking_track[id]:
                                    for index,i in enumerate(booking_track[id][service_cu][Current_User]):
                                        if i[:-2] in (list(confirm_exchange[Current_User][req_user].keys())[0]):
                                            booking_track[id][service_cu][req_user].append(booking_track[id][service_cu][Current_User][index])
                                            del booking_track[id][service_cu][Current_User][index]
                                            for s_num,s in enumerate(sell_list[Current_User]):
                                                if (s.split("_",1)[1])[:-2]==i:
                                                    del sell_list[Current_User][s_num]
                                                if not sell_list[Current_User]:
                                                    del sell_list[Current_User]
                                                

                                if service_ru in booking_track[id]:
                                    for index,i in enumerate(booking_track[id][service_ru][req_user]):
                                        if i[:-2] in (list(confirm_exchange[req_user][Current_User].keys())[0]):
                                            booking_track[id][service_ru][Current_User].append(booking_track[id][service_ru][req_user][index])
                                            del booking_track[id][service_ru][req_user][index]
                                            for s_num,s in enumerate(sell_list[req_user]):
                                                if (s.split("_",1)[1])[:-2]==i:
                                                    del sell_list[req_user][s_num]
                                                if not sell_list[req_user]:
                                                    del sell_list[req_user]
                                                
                            return booking_track
                    else:
                        print(f"\nWait for {req_user} to proceed!")
                        confirm_exchange[Current_User][req_user]={booking_to_exchange:''} 
                        return booking_track                               
            else:
                if Current_User not in confirm_exchange:
                    confirm_exchange[Current_User]={}
                    confirm_exchange[Current_User][req_user]={booking_to_exchange:''}
                    print(f"\nExchange request has been sent from your side, If {req_user} accepts, exchange process will proceed\n")
                    return booking_track
                else:
                    print(f"\nYour request has already been sent, Please wait for {req_user} to proceed ")
                    return booking_track
                #confirm_exchange[Current_User][req_user]={}

            

        else:
            print(f"\nYou have no message history with {req_user}, you cannot exchange with them")
            return booking_track
        


            
def msg_all(msg,current_user,pool):
    for user in pool:
        if(current_user != user):
            message_dict[user][current_user].append(msg)
            
def  Complaintbox(role):
    global message_dict
    
    options=['View Complaints', 'Message users']
   
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    while True:
        try:
            selected_opt = int(input("\nEnter your choice: "))
            if selected_opt>len(options) or selected_opt<0:
                print("\nInvalid entry, try again!")
            else:
                break
        except:
            print("Please enter an integer value")

    if selected_opt==1:
        count=0
        
        for i in message_dict['admin']:
            if len(message_dict['admin'][i])!=0:
                count+=1
                for id,msg in enumerate(message_dict['admin'][i]):
                    print(f"{i} : {message_dict['admin'][i][id]}")
        if count==0: print("No Complaints!")

    if selected_opt==2:
        message('admin',booking_track)


if __name__ == '__main__':
    
    while True:
       
        print("\nHello, Welcome to our seat booking application!\n")
        print("\nPlease enter your login credentials")
        role = authenticate()
        if role=='admin':
            name='admin'
        else:
            name = role.split('_')[1]
        print(f"\nWelcome {name}!")

        if role.split('_')[0] == 'owner':
            while True:
                options=['Add Service','View Existing Services','Send a complaint']
                for i, option in enumerate(options):
                    print(f"{i+1}. {option}")

                while True:
                    try:
                        selected_opt = int(input("\nEnter your choice: "))
                        if selected_opt>len(options) or selected_opt<0:
                            print("\nInvalid entry, try again!")
                        else:
                            break
                    except:
                        print("Please enter an integer value")

                if selected_opt==1:

                    while True:
                        service, size, reg_price = get_owner_details()

                        if name not in available_rooms:
                            available_rooms[name]={}
                            booking_track[name]={}
                            available_rooms[name][service]={}
                            booking_track[name][service]={}
                            available_rooms[name][service]['price_for_each_seat']= [];available_rooms[name][service]['dates'] =[]; available_rooms[name][service]['times']=[]; #available_rooms[name]['messages'] =[]
                            break
                    
                        elif service not in available_rooms[name]:
                            available_rooms[name][service]={}
                            booking_track[name][service]={}
                            available_rooms[name][service]['price_for_each_seat']= [];available_rooms[name][service]['dates'] =[]; available_rooms[name][service]['times']=[]; #available_rooms[name]['messages'] =[]
                            break
                        else:
                            print("\nService already exists, try again!")
                    

                    o = owner(service, size, reg_price)
                    available_rooms[name][service]['dates']=o.select_dates()
                    available_rooms[name][service]['times']=o.select_times()
                    for i in range(len(available_rooms[name][service]['dates'])*len(available_rooms[name][service]['times'])):
                        available_rooms[name][service]['price_for_each_seat'].append(o.set_price())
                    

                    ans = str(input("\nYour details are saved! \nPress 'b' to go back to main menu or anyother key to quit"))
                    if ans=='b':
                        continue
                    else:
                        break
                            

                if selected_opt==2:
                    if name in available_rooms:
                        print(available_rooms[name])
                    else:
                        print("\nNo existing rooms")
                    ans = str(input("\nPress 'b' to go back to main menu or anyother key to quit"))
                    if ans=='b':
                        continue
                    else:
                        break

                if selected_opt==3:
                    message(name,booking_track)
                    ans = str(input("\nYour details are saved! \nPress 'b' to go back to main menu or anyother key to quit"))
                    if ans=='b':
                        continue
                    else:
                        break

        if role.split('_')[0] == 'user':
                u = user(name)
                while True:
                    available_rooms, booking_track, sell_list,sl_watchers = u.get_action(available_rooms, booking_track, sell_list,sl_watchers)
                    ans = str(input("\n If you want to go back, enter b \n otherwise press q to exit: "))
                    if ans == 'b':
                        continue
                    else:
                        break
        
        if role == 'admin':
            adm=Admin()
            while True:
                admin_tasks  = ['View Bookings','Modify Bookings','View Business','View Sell List', 'View Confirm Resell Requests', 'View Confirm Exchange Requests', 'View Sell list Watchers','View Complaints']
                for i, task in enumerate(admin_tasks): print(f"{i+1}. {task}")
                while True:
                    try:
                        activity = int(input("\nPlease Select an option: "))
                        if activity>len(admin_tasks) or activity<0:
                            print("\nInvalid choice, Try again!\n")
                        else:
                            break
                    except:
                        print("\nInvalid choice, Try again!\n")

            
                if activity == 1:
                    adm.view_bookings()
                    ans = str(input("\n If you want to go back, enter b \n otherwise press any other key to exit: "))
                    if ans == 'b':
                        continue
                    else:
                        break
                elif activity == 2:
                    adm.modify_bookings()
                    ans = str(input("\n If you want to go back, enter b \n otherwise press any other key to exit: "))
                    if ans == 'b':
                        continue
                    else:
                        break
                elif activity == 3:
                    adm.view_business()
                    ans = str(input("\n If you want to go back, enter b \n otherwise press any other key to exit: "))
                    if ans == 'b':
                        continue
                    else:
                        break
                elif activity == 4:
                    adm.view_sell_list()
                    ans = str(input("\n If you want to go back, enter b \n otherwise press any other key to exit: "))
                    if ans == 'b':
                        continue
                    else:
                        break
                elif activity == 5:
                    adm.view_confirm_resell_requests()
                    ans = str(input("\n If you want to go back, enter b \n otherwise press any other key to exit: "))
                    if ans == 'b':
                        continue
                    else:
                        break
                elif activity == 6:
                    adm.view_confirm_exchange_requests()
                    ans = str(input("\n If you want to go back, enter b \n otherwise press any other key to exit: "))
                    if ans == 'b':
                        continue
                    else:
                        break
                
                elif activity == 7:
                    adm.view_sell_list_watchers()
                    ans = str(input("\n If you want to go back, enter b \n otherwise press any other key to exit: "))
                    if ans == 'b':
                        continue
                    else:
                        break
                
                elif activity == 8:
                    Complaintbox('admin')
                    ans = str(input("\n If you want to go back, enter b \n otherwise press any other key to exit: "))
                    if ans == 'b':
                        continue
                    else:
                        break            
        continue

#add business class of seat in sell list