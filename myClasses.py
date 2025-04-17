class Arithmetics:
    def __init__(self,numberA:float,numberB:float):
        self.numberA=numberA
        self.numberB=numberB
    def addition(self):
        return self.numberA + self.numberB
    def subtract(self):
        return self.numberA-self.numberB
    def multiply(self):
        return self.numberA * self.numberB
    def divide(self):
        return self.numberA/self.numberB

class Car:
    def __init__(self,parameter1,parameter2):
        self.property1=parameter1
        self.property2=parameter2
    def drive(self):
        x= self.property1+self.property2
        print(f"Speed is {x}")

class App:
    def __init__(self,users:int,username:str,storage:float):
        self.users=users
        self.username=username
        self.storage=storage
    def login(self):
        if self.users>=1 and self.username=="Abdiel":
            print("Welcome Admin!!")
            print(f"Your storage is {self.storage} MB")
        else:
            print(f"Access denied!! You are not an admin, but an imposter called {self.username}! Back off you imposter!")
    
    def increase_storage(self,number:float):
        self.storage+=number
        print(f"Storage increased. New storage is {self.storage} MB")
        
    