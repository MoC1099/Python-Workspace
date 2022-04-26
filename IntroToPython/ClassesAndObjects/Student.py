#this is the student data type/ student file

class Student:
    #this is the initialized function
    def __init__(self, name, major, GPA, is_on_probation):
        #the actual objects name is gonna be = the name they passed
        #the name of the student = to the name that we passed in
        self.name = name
        #the major of the student = to the major that we passed in
        #self is refering to the actudal object
        self.major = major
        self.GPA = GPA
        self.is_on_probation = is_on_probation