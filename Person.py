class Person:
    def __init__(self,name,age,promise):
        self.name = name
        self.age = age
    
    def set_username(self,name):
        self.name = name
    
    def get_username(self):
        return self.name
    
    def set_age(self,age):
        self.age = age
    
    def get_age(self):
        return self.age
    
    def set_promise(self,promise):
        self.promise = promise
    
    def get_promise(self):
        return self.promise
    
    
me = Person("Kopano",20,None)
me.set_promise("I want to go to the gym")
print(me.get_promise())
