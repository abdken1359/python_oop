class Travel:
    def __init__(self,country:str,month:str,type:str):
        self.country=country
        self.month=month
        self.type=type
        self.season=""
        self.cost=0
        self.months=("January","February","March","April","May","June","July","August","September","October","November","December")
        self.winter_months=("October","November","December","January","February","March")
        
       
       
    def trip_infos(self):
        print(f"Country: {self.country}")
        print(f"Month: {self.month}")
        
        for winter in self.winter_months:
            if self.month.lower() == winter.lower():
                self.season="Winter"
                break
        if self.season!="Winter":
            self.season="Summer"
            
        print(f"Season: {self.season}")
        print(f"Type of travel: {self.type}")
    def calc_cost(self,cost):
        self.cost+=cost
        
        additional_cost=float(input("Enter aditional cost :  "))
        self.cost+=additional_cost
        if self.cost <500:
            print("Low budget!")
        elif self.cost >=500 and self.cost<=1500:
            print("Enjoy a flight anywhere!")
        else:
            print("Luxury trip!")
            
        
    
