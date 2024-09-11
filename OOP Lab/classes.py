from HandleEmail import check_email

class Person:
    moods=("happy","tired","lazy")
    def __init__(self,name, money, mood, healthRate):
        self.name=name
        self.money=money
        self.mood=mood
        self.healthRate=healthRate

    def sleep(self, sleepHour):
        if sleepHour.isdigit():
            sleepHour = int(sleepHour)
        if sleepHour == 7:
            self.mood = Employee.moods[0]
        elif sleepHour < 7:
            self.mood = Employee.moods[1]
        elif sleepHour > 7:
            self.mood = Employee.moods[2]
        print(f"{self.name} is {self.mood} after sleeping {sleepHour}")

    def eat(self,meals):
        if meals == 3 :
            self.healthRate=100
        elif meals == 2 :
            self.healthRate=75
        elif meals == 1 :
            self.healthRate=50
        print(f"{self.name}'s health rate is now {self.healthRate}% after eating {meals} meals.")



class Office:
    Number_of_emp=len(self.employees)
    def __init__(self,off_name,employees):
        self.off_name=off_name
        self.employees=employees
        self.Add_Employee()

    def Add_Employee(self):
        try:
            fileobject=open(f"{self.off_name}_Emp.txt","w")
        except Exception as e:
            print(e)
            return False
        else:
            fileobject.writelines(self.employees)
            fileobject.close()
            return True

    def get_all_employees(self):
        try:
            fileobject=open(f"{self.off_name}_Emp.txt","r")
        except Exception as e:
            print(e)
            return False
        else:
            data=fileobject.readlines()
            for emp in data:
                print(emp)




class Car:
    def __init__(self, car_name ,fuelRate, velocity):
        self.car_name=car_name
        self.fuelRate=fuelRate
        self.velocity=velocity

    # def run(self,velocity,distance):
    #     self.velocity=velocity
    #     self.fuelRate = self.fuelRate - self.fuelRate*0.1
    #     distance -= 1
    #     return dis
    #
    # def stop(self):
    #     self.velocity=0
    #     print("Car will stop...")
    #     print(f"remain distance: {}")





class Employee(Person):
    def __init__(self, name, money, mood, healthRate,id ,car ,email ,salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id=id
        self.car=car
        self.email=email
        self.salary=salary
        self.distanceToWork=distanceToWork

    def work(self,workHour):
        if workHour == 8 :
            self.mood=Employee.moods[0]
        elif workHour < 8 :
            self.mood=Employee.moods[2]
        elif workHour > 8 :
            self.mood=Employee.moods[1]
        print(f"{self.name} is {self.mood} after working for {workHour} hours.")

    def buy(self,items):
        cost = items *10
        if self.money >cost:
            self.money = self.money - cost
        print(f"{self.name} bought {items} items, costing {cost}. Remaining money: {self.money}.")

    def send_mail(self,to, subject, msg, receiver_name):
        try:
            while not check_email(to) :
                print("Invalid Email")
                to=input("Input a valid email: ")
            fileobject = open("mail.txt", "w")
        except Exception as e:
            print(e)
            return False
        else:
            fileobject.writelines(f"From:{self.email}\n To: {to} \n \nHi {receiver_name}\n{msg}\n{subject} ")
            fileobject.close()
            return True

    def drive(self,time):
        velocity=self.distanceToWork * time
        if velocity !=0 :
            Car.velocity = velocity
        Car.run(Car.velocity, self.distanceToWork)
        # return self.distanceToWork , velocity

    def refuel (self):
        #self.car.fuelRate=100
        super().fuelRate=100


