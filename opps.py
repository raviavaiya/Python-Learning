# class Student:
#     # default constructor
#     # def __init__(self):
#     #     print("Constructor is called !!!!")
#     #     pass

#     # Parameterized Constructor
#     college_name="Jain University"
#     name="anonymous" # Class Attribute
#     def __init__(self,fullname, marks):
#         self.name=fullname # obj Attribue > class attribute
#         self.marks=marks
#         print("Constructor is called !!!!")

#     def get_marks(self):
#         return self.marks

#     def hello(self):
#         print("Hello",self.name, s1.get_marks())

    
# s1 = Student("Ravi",90)
# print(s1.name)
# print(Student.college_name)
# s1.hello()
# print(s1.get_marks())

# Methods

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def get_average(self):
#         sum=0
#         for val in self.marks:
#             sum += val
#         print("hii",self.name, "your average score is :",sum/3)

# s1=Student("Ravi Avaiya",[99,90,85])
# s1.get_average()

#Static Methods

# class Student:
#     @staticmethod #decorator
#     def hello():
#         print("Hello, I am a static method !!!!")

# s1=Student()
# s1.hello()


# OOPs  Concepts
# 1. Inheritance


# 2. Polymorphism
    


# 3. Abstraction
     # Hiding Unnecessary code
     # Only showing the essential features to user

# class Car:
#     def __init__(self):
#         self.accerator=False
#         self.Break=False
#         self.Clucth=False
    
#     def start(self):
#         self.Clucth=True
#         self.accerator=True
#         print("Car started")

#     def stop(self):
#         self.accerator=False
#         self.Break=True
#         print("car stopped")

# c1=Car()
# c1.start()
# print("Car running on Highway...")
# c1.stop()



# 4. Encapsulation
    # Wrapping data and functions into a single object (unit)



class Account:
    def __init__(self, balance, account_number):
        self.__balance = balance
        self.__account_number = account_number
    
    def  get_balance(self):
        return self.__balance
    def deposit(self, amount):
        self.__balance += amount
        print("Rs.",amount,"Was  deposited")
        print("total balance",self.__balance)
    def  withdraw(self, amount):
        if amount > self.__balance:
            print("Not Sufficient Balance...")
            print("total balance",self.__balance)
        else:
            self.__balance-=amount
            print("Rs.",amount,"Was  withdrawn")
            print("total balance",self.__balance)

a1=Account(10000,1245)
a1.deposit(8000)   
a1.withdraw(5000)
