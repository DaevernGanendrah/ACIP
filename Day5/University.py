class Person:
    def __init__(self,name):
        self.Name = name

class Student(Person):
    def __init__(self,name,cgpa):
        super(Student,self).__init__(name)
        self.CGPA = cgpa

class Staff(Person):
    def __init__(self,name,salary):
        super(Staff,self).__init__(name)
        if(salary<1100):
            raise Exception("Salary ${} too low!".format(salary))
        self.Salary = salary

class Lecturer(Staff):
    def __init__(self,name,salary,allowance):
        super(Lecturer,self).__init__(name,salary)  #Constructor chaining
        self.Allowance = allowance

class Clerk(Staff):
    def __init__(self,name,salary,otRate):
        super(Clerk,self).__init__(name,salary)  #Constructor chaining
        self.OTRate = otRate
        self.OTHours = 0

class Manager(Staff):
    def __init__(self,name,salary,carAllowance):
        super(Manager,self).__init__(name,salary)
        self.CarAllowance = carAllowance
    def getMonthlySalary(self):
        return (1.0-0.11)*self.Salary + self.CarAllowance

class HRManager(Manager):
    def __init__(self,name,salary):
        super(HRManager,self).__init__(name,salary,500)

class SalesManager(Manager):
    def __init__(self,name,salary,carAllowance,petrolAllowance):
        super(SalesManager,self).__init__(name,salary,carAllowance)
        self.PetrolAllowance = petrolAllowance
        self.MonthlySales = 0.0

m = Manager("Ali",5000,600)
print("Name:{}\tMonthly Salary:${}".format(m.Name,m.getMonthlySalary()))

hrm = HRManager("Ahmad",4000)
print("Name:{}\tMonthly Salary:${}".format(hrm.Name,hrm.getMonthlySalary()))

sm = SalesManager("Abu",5000,600,800)
sm.MonthlySales = 100000
print("Name:{}\tMonthly Salary:${}".format(sm.Name,sm.getMonthlySalary()))

