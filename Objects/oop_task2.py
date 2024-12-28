class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
        
    def showDetails(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)
        
e1=Employee("manager","Finanace",300000)    
e1.showDetails()    
    
class Engineer(Employee): 
    def __init__(self,name,age):
        self.name=name
        self.age=age 
        super().__init__("Engineer","IT",50000)  

        
        
eng1=Engineer("MARK",34)
eng1.showDetails()           