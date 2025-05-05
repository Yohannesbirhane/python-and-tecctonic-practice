# #creating a class 
# class ClassName:
#     pass
# print (ClassName)
# print (type(ClassName))
# ## creating an object
# #We can create an object by calling the class
# h=ClassName()
# print (h)
# ## constructor 
# class Animal:
#     def __init__ (self,name):
#         self.name=name
# animal1=Animal("lion")        
# print (animal1.name)
##Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income,
# total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description.
# # The same goes for expenses.
# class PersonAccount:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.incomes = []  # A list of dictionaries to store income details
#         self.expenses = []  # A list of dictionaries to store expense details

#     def add_income(self, amount, description):
#         """Adds an income entry with an amount and description."""
#         self.incomes.append({"amount": amount, "description": description})
    
#     def add_expense(self, amount, description):
#         """Adds an expense entry with an amount and description."""
#         self.expenses.append({"amount": amount, "description": description})

#     def total_income(self):
#         """Calculates the total income."""
#         return sum(income['amount'] for income in self.incomes)

#     def total_expense(self):
#         """Calculates the total expense."""
#         return sum(expense['amount'] for expense in self.expenses)

#     def account_balance(self):
#         """Calculates the account balance."""
#         return self.total_income() - self.total_expense()

#     def account_info(self):
#         """Returns a summary of the account."""
#         return {
#             "Full Name": f"{self.firstname} {self.lastname}",
#             "Total Income": self.total_income(),
#             "Total Expense": self.total_expense(),
#             "Account Balance": self.account_balance()
#         }


# # Example usage
# person = PersonAccount("John", "Doe")
# person.add_income(5000, "Salary")
# person.add_income(200, "Freelance Work")
# person.add_expense(1000, "Rent")
# person.add_expense(200, "Utilities")

# print(person.account_info())
## bank system 

# class library ():
#     def __init__(self, name, place):
#         self.name=name
#         self.place=place
#         pass
# lib1=library('tesfa','gibi')
# print(lib1.name)
# print(lib1.place)
'''## create abook class that store tittele,author ,publication year
class book:
    def __init__(self,title,author,publication_year):
        self.title=title
        self.author=author
        self.publication_year=publication_year
  
    def display_ditails (self):
       print(f"{self.title} book is written by {self.author} in {self.publication_year}")  
book1=book("fikr eske mekabr","addis alemayehu","1990")     '''
#book1.display_ditails()
###
# class laptop:
#     def __init__(self,model,genen,ram ):
#         self.model=model
#         self.genen=genen
#         self.ram=ram
#     def buy(self):
#         print(f"I bought anew laptop of model {self.model}   {self.genen} and have {self.ram} ram")  
         
# pc1=laptop("hp elite book","8th generation","16 GB ")  
# pc1.buy()      
# ## inheritance
# class animal :
#     def __init__(self ,name,color):
#         self.name=name
#         self.color=color
#     def drink(self):
#         print (f"the {self.color} {self .name} cat is drink the milk")
# class cat (animal):
#     def run (self):
#         print (f"the {self.name } cat run quickly")
# my_cat=cat ("love","white")
# my_cat.drink() 
# my_cat .run()      

'''## bank system
class account:
    def __init__ (self ,owner,balance):
        self.owner=owner
        self.balance=balance
    def  deposite(self ,amount ):
        self.balance+=amount
        if amount >0:
             print (f"added {amount} to the balance")
        else:
            print("invalid amount is added")     
    def get_balance(self):
         return self.balance
my_account=account("yohannes",20000)
my_account.deposite(40000)
print ( "current balance is"  ,my_account.get_balance()) '''       
# class Animal:
#     def __init__(self ,name):
    
#         self.name =name
# anim1=Animal  ("camel")
# anim2=Animal("horse")
# anim3=Animal("donkey")
# print (anim1.name)
# print (anim2.name)
# print (anim3.name)
# ##multiple parametre in the  constractor
'''class person:
    def __init__ (self ,first_name,last_name ,age ,country,city):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
        self.city=city
person1=person("yishaq"," boss",45,"Ethiopia","Debre Berhan")
person2=person("yohannes","John",65,"Ethiopia","Debre Berhan")

print  (person1.first_name,person1.last_name, person1.age,person1.country, person1.city)    

print  (person2.first_name,person2.last_name, person2.age,person2.country, person2.city)
     
'''
##Build a Student class that holds a student's name, age, grades (in a dictionary), and enrolled courses (a list). 
# Create an instance of a student and print their name, age, and grades.
class student :
    def __init__(self,name,age,grade,enrolled_courses):
        self.name =name 
        self. age=age
        self.grade=grade
        self.enrolled_courses=enrolled_courses
    def details( self):
        print (f"student name {self.name} i am  {self.age }years old  my grade is {self.grade } and i learn {self.enrolled_courses}")
stund =student( "yohannes",22,{" programing" :"A+" ,  "disecret" :"A+"} ,[" logic","psychology"])
stund.details()
## abstraction 
from abc import ABC,abstractmethod    
class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    def stop_engine(self):
        pass
class car (vehicle):
    def start_engine(self):
        print (" car move")
    def stop_engine(self):
        print ( "car stop")
car=car() 
car.stop_engine()
### encapsulation 
class car :
    
     

        