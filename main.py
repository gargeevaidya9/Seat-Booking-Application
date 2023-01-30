import math
import numpy as np

class owner:
    def __init__(self, size, price):
        self.size = size
        self.price = price
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
    owners = {}
    users={}
    print("Hello, Welcome to our seat booking application!\n")
    print("Please enter your login credentials")
    role = authenticate()
    name = role.split('_')[1]
    print(f"Welcome {name}!")
    if role.split('_')[0] == 'owner':
        owners[name]={}
        size = int(input("\nEnter size of the room: "))
        reg_price = int(input("\nEnter regular price: "))
        o = owner(size, reg_price)
        owners[name]['price'] = o.set_price()
        
    





        

    
  
    
