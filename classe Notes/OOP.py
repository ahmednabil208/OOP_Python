print() #new line
#==================================OOP=================================================
"Create Class"
class Employee:
    pass

"Take an object from class Employee"
emp1=Employee()  #Adress of Object
print(f"Object emp1: {emp1} ")
print(f"Class Employee is {Employee}")
###############################################################################################################
"self"
class Employee:
    def __init__(self):
        print(self)  # self: refer to the object address in the memory

emp1=Employee()
print(emp1)


###############################################################################################################
"Constructor is a method called at the moment an object is instantiated."
class Employee:
    def __init__(self):  #__init__ --> Constructor Function
        print("Hi Ahmed")

emp1=Employee()
###############################################################################################################
"Print object values"
class Employee:
    def __init__(self,name,salary,dept,address):
        self.name=name      #instance variable
        self.salary=salary
        self.dept=dept
        self.address=address


emp1=Employee(name="Ahmed",salary=15000,dept="Cloud",address="Giza")
print(emp1.name)
print(emp1.salary)
print(emp1.dept)
print(emp1.address)
###############################################################################################################
"Convert class into dictionary "
class Employee:
    def __init__(self,name,salary,dept,address):
        self.name=name      #instance variable
        self.salary=salary
        self.dept=dept
        self.address=address


emp1=Employee(name="Ahmed",salary=15000,dept="Cloud",address="Giza")
emp1=emp1.__dict__
print(emp1)
###############################################################################################################
"Class variables"
class Employee:
    count=0   #class variable
    def __init__(self,name,salary,dept,address):
        self.name=name      #instance variable
        self.salary=salary
        self.dept=dept
        self.address=address
        Employee.count += 1 #access class variable using class name

emp1=Employee(name="Ahmed",salary=15000,dept="Cloud",address="Giza")
emp2=Employee(name="Ali",salary=10000,dept="Devops",address="Cairo")

print(f"Number of employees: {Employee.count}")  #access class variable using class name
##############################################################################################################
"Change Class variables"
class Employee:
    Test=True   #class variable
    def __init__(self,name,salary,dept,address):
        self.name=name      #instance variable
        self.salary=salary
        self.dept=dept
        self.address=address


emp1=Employee(name="Ahmed",salary=15000,dept="Cloud",address="Giza")
emp2=Employee(name="Ali",salary=10000,dept="Devops",address="Cairo")

print(f"employee 1: {emp1.Test}")
print(f"employee 2: {emp2.Test}")
print("=============================================")
emp1.Test=False
print(f"employee 1: {emp1.Test}")
print(f"employee 2: {emp2.Test}")
print("=============================================")
emp1.Test=True
print(f"employee 1: {emp1.Test}")
print(f"employee 2: {emp2.Test}")
############################################################################################################

"Instance Method"
class Employee:
    def __init__(self,name,salary,dept,address):
            self.name=name      #instance variable
            self.salary=salary
            self.dept=dept
            self.address=address

    "Instance Method"
    def calc_taxes(self):
        return self.salary*0.2

emp1=Employee(name="Ahmed",salary=15000,dept="Cloud",address="Giza")
print(f"Taxes: {emp1.calc_taxes()}")

###########################################################################################################

"Class Method"
class Employee:
    def __init__(self,name,salary,dept,address):
            self.name=name      #instance variable
            self.salary=salary
            self.dept=dept
            self.address=address

    "Class Method"
    @classmethod
    def create_employee_from_string(cls,data):
        split_data=data.split(":")
        #can use Employee instead of cls
        return cls(split_data[0],split_data[1],split_data[2],split_data[3])

mydata= "Ahmed:15000:cloud:Giza"
emp=Employee.create_employee_from_string(mydata)
print(f"Employee information: {emp.name}, {emp.salary}, {emp.address}, {emp.dept}")

###################################################################################################

"Static Method"


##############################################################################################################

"Inheritance"

class Employee:
    def __init__(self,name,salary,dept,address):
            self.name=name      #instance variable
            self.salary=salary
            self.dept=dept
            self.address=address

class Accountant(Employee):   #Inheritance
        def __init__(self, safe, name, salary, dept, address):  #add safe (instance variable)
            self.safe=safe
            self.name = name  # instance variable
            self.salary = salary
            self.dept = dept
            self.address = address

#######################################################################################################

class Employee:
    def __init__(self,name,salary,dept,address):
            self.name=name      #instance variable
            self.salary=salary
            self.dept=dept
            self.address=address


class Accountant(Employee):
    def __init__(self,safe,name,salary,dept,address):
        super().__init__(name,salary,dept,address)
        self.safe=safe


acc1=Accountant(name="ahmed",salary=15000,safe="safe1",dept="cloud",address="Giza")
print(acc1.safe)
print(acc1.name)


########################################################################################################################
#
"Overriding"

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def calc_taxes(self):
        print("in Employee")
        return self.salary *0.1

class Accountant(Employee):
    def __init__(self,name,salry,safe):
        super().__init__(name,salry)
        self.safe=safe

    def calc_taxes(self):
            print("in Accountant")
            original_taxes=super().calc_taxes()
            return original_taxes +100


acc1=Accountant(name="Ahmed",salry=15000,safe="safe1")
print(acc1.calc_taxes())




########################################################################################################################################

class Employee:

    pass

emp1=Employee

print(emp1)
########################################################################################################################################

def FdevBy3(num):
    if num%3==0:
        return True
    return False

def SdevBy3(num):
    return num %3 == 0


TdevBy3=lambda num: num%3==0   #One Line


print("First Method: ",FdevBy3(6))
print("Second Method: ",SdevBy3(6))
print("Third Method: ",TdevBy3(6))
########################################################################################################################################

"Lambda with filter function"

check_div_by_three =lambda num : num%3==0
my_num=[1,3,5,7,9]

for val in filter(check_div_by_three,my_num):
    print(val)

"Better Method"

my_num=[1,3,5,7,9]
for val in filter(lambda val : val%3==0,my_num):
    print(val)


########################################################################################################################################

"lambda with map function"
my_num=[1,3,5,7,9]
output=map(lambda num : num **2, my_num)
print(list(output))

print