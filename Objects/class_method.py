class Person:
    name="anonymous"
    
    # def change_name(self,name):
        # self.name=name # new name atributr create kore
        # self.__class__.name=name #class mehod use kore oi class er attribute er name assign kore
        # Person.name="Rahul" #same as above
    @classmethod
    def change_name(cls,name):
         cls.name=name   
        
p1=Person() #object cretation
p1.change_name("Promi")
print(p1.name)
print(Person.name)        
        