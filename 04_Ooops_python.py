# class Example:
#     def __init__(self,num):
#         self.num=num

#     def set_num(self,num):
#         self.num=num

#     def get_num(self):
#         return self.num
    

# obj=Example(10)
# print(obj.get_num())
# obj.set_num(15)
# print(obj.get_num())

# class customer:
#     def __lnit__(self,id):
#         self.id=100
# cl=customer(200)
# print(cl.id)

# class customer:
#     def __init__(self,id):
#         self.id=id

# cl=customer(200)
# print(cl.id)

# class shoe:
#     def __init__(self, price, material):
#         self.price = price
#         self.material = material

# s1=shoe(1000, "canvas")
# print("the unique id of the object",id(s1))
# print(s1)
# print(s1.price,s1.material)


# class shoe:
#     def __init__(self, price, material):
#         self.price = price
#         self.material = material

#     def __str__(self):
#         return "shoe with price:" + str(self.price)+"  and material:   " + self.material
    
# s1=shoe(1000,"canvas")
# print(s1)

# class Mobile:
#     def _init_(self,brand,price):
#         self.brand = brand
#         self.price = price
#         self.total_price = None
#     def purchase(self):
#         if self.brand == "apple":
#             discount = 10
#         else:
#             discount = 5
#         self.total_price = self.price - self.price *(discount/100)
#         print("Total price of",self.brand,"mobile is",self.total_price)

# mob1=Mobile("apple",20000)
# mob2=Mobile("samsung",10000)
# mob1.purchase()
# mob2.purchase()

# print(mob1.amount_returned())


# class Customer:
#     def __init__(self,cust_id,name,age,wallet_balance):
#         self.cust_id = cust_id
#         self.name = age
#         self.wallet_balance = wallet_balance
#     def update_balance(self,amount):
#         if amount < 1000 and amount > 0:
#             self.wallet_balance += amount
#     def show_balance(self):
#         print("the balance is ",self.wallet_balance)

# c1=Customer(100,"Gopal",24,1000)
# c1.update_balance(500)
# c1.show_balance()



# class Customer:
#     def __init__(self,cust_id,name,age,wallet_balance):
#         self.cust_id = cust_id
#         self.name = age
#         self.wallet_balance = wallet_balance
#     def set_balance(self,amount):
#         if amount < 1000 and amount > 0:
#             self.wallet_balance += amount
#     def get_wallet_balance(self):
#         print("the balance is ",self.wallet_balance)

# c1=Customer(100,"Gopal",24,1000)
# print(c1.get_wallet_balance())
# c1.set_balance(5000)
# print(c1.get_wallet_balance())



# class Dam:
#     def __init__(self,name, length):
#         self.name=name
#         self.__length=length
#     def get_length(self):
#         return self.__length
# dam1=Dam("ABC dam",3.5)
# print("Dam name:",dam1.name)
# print("Dam Length", dam1.length())


# class Table:
#     def __init__(self):
#         self.no_OF_legs=4
#         self.__glass_top=None
#         self.__wooden_top=None
#     def assign_data(self,glass_top,wooden_top):
#        self.__glass_top=glass_top
#        self.__wooden_top=wooden_top
#     def identify_rate(self,glass_top,wooden_top):
#         self.assign_data(glass_top,wooden_top)
#         if(self.__glass_top==True):
#             rate=20000
#         elif(self.__wooden_top==True):
#             rate=30000 
#         else:
#             rate=0
#         return rate
# dining_table=Table()
# rate=dining_table.identify_rate(False,True)
# print(rate)



class Table:
    def __init__(self):
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None
dining_table=Table()
back_table=Table
front_table=back_table
back_table=dining_table
print(id(dining_table),id(back_table),id(front_table))                               