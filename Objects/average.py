class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def count_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"Your score is",format(sum / 3, ".2f"))  
               
        
s1=Student("Mugdho",[99,90,70])  
s1.count_avg()      