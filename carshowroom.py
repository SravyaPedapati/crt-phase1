class classroom:
    def __init__(self):
        self.cgst=0.18
        self.sgst=0.18
        self.insurance=100000
    def company(self):
        while True:
            print("select a car from Ferrari Mahindra Volvo")
            self.n=input("select a car ")
            if self.n=="Ferrari":
                print("Welcome to Ferrari")
                self.model()
                break
            elif self.n=="Volvo":
                print("Welcome to Volvo")
                self.model()
                break
            elif self.n=="Mahindra":
                print("Welcome to Mahindra")
                self.model()
                break
            else:
                print("enter valid data")

    def model(self):
        if self.n=="Ferrari":
            while True:
                print("select a car from GTB ROMA")
                self.choice=input("your desired car")
                if self.choice=="GTB":
                    self.price(self.choice)
                    break
                elif self.choice=="ROMA":
                    self.price(self.choice)
                    break
                else:
                    print("enter available model")

        if self.n=="Volvo":
            while True:
                print("select a car from XC90 S90")
                self.choice=input("your desired car")
                if self.choice=="XC90":
                    self.price(self.choice)
                    break
                elif self.choice=="S90":
                    self.price(self.choice)
                    break
                else:
                    print("enter a valid model")


        if self.n=="Mahindra":
            while True:
                print("select a car from SCORPIO THAR")
                self.choice=input("your desired car")
                if self.choice=="SCORPIO":
                    self.price(self.choice)
                    break
                elif self.choice=="THAR":
                    self.price(self.choice)
                    break
                else:
                    print("enter a valid model")

    def price(self,choice):
        if choice=="GTB":
            self.price=24000000
        elif choice=="ROMA":
            self.price=2356780
        elif choice=="XC90":
            self.price=3575670
        elif choice=="S90":
            self.price=34234869
        elif choice=="SCORPIO":
            self.price=4237890
        elif choice=="THAR":
            self.price==12378900
        tot_p = self.price+(self.sgst)*self.price+(self.cgst)*self.price+self.insurance
        print(tot_p)









obj=classroom()
obj.company()
    

