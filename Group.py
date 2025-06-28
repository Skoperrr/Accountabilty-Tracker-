import Person
class Group:
    group_name = ""
    group_list = []
    person = Person()
    def __init__(self,group_name,group_dict,person):
        self.group_name = group_name
        self.group_dict = group_dict
        self.person = person
    
    def create_group(self,name):
        self.group_name = name
    
    def add_people_to_group(self,person):
        self.group_dict["Username"] = person.get_username()
        self.group_dict["Age"] = person.get_age()

    def remove_person_from_group(self,person):
        self.group_dict.pop(person)



        
