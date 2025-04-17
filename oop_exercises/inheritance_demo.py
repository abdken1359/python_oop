class Animal:
    def __init__(self,region:str , animal_type:str, color:str, lethal:bool):
        self.region=region
        self.animal_type=animal_type
        self.color=color
        self.lethal=lethal
        print(f"Hello world!{self.region}")
    def animal_bio(self):
        print("Animal Passport:")
        print(f"Found in : {self.region}")
        print(f"Species: {self.animal_type}")
        print(f"Color: {self.color}")
        print(f"Dangerous : {self.lethal}")
class Clinic(Animal):
    def search(self,animals:list):
        print(animals)

dog=Animal("Cameroon","German shepherd","Orange",True)
print(dog)