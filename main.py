## Without using class format, we cannot use templates of class

# class Employee:
#     pass

# ramesh = Employee()
# suresh = Employee()

# ramesh.fname = "Ramesh"
# ramesh.lname = "Kumar"
# ramesh.salary = "10000"

# suresh.fname = "Suresh"
# suresh.lname = "Kaushik"
# suresh.salary = "20000"

# print(ramesh.fname)
# print(suresh.fname)

# print("_"*50)

# print(ramesh)
# print(suresh)


#___________________________________

#With the use of class concept

class Employee:

    increment = 1.5
    no_of_employee = 0

    def __init__(self, fname, lname, salary):  # Constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 2
        Employee.no_of_employee += 1

    def increase(self):  # IF we will remove self argument then we cannot call this method with empty function
                        # call, because function call with methods sends, "self" paramter by default
                        # in python

        '''
        self.increment:
         It will first search if there is any instance or variable is in constructor
        if it will not find then it will search class variable which is outside any methods.

        Employee.increment:
         It will only use variable or instance which are outside any methods.
        '''                
        self.salary = int(self.salary * self.increment) 
        #if we will use increment variable directly
        #then it will give error and if we use self.increment 
        # then it will check contructor variable then class
        #variable


        self.salary = int(self.salary * Employee.increment)  
        # # We can use Employee class to use variable
        # which are not under any methods


print(Employee.no_of_employee)  # To use class variable we use class name directly
ramesh = Employee("Ramesh","Kumar",10000)
print(Employee.no_of_employee)
suresh = Employee("Suresh","Kaushik",20000)
print(Employee.no_of_employee)  # It is incrementing each time any object creating



# print(ramesh.fname)
# print(suresh.fname)
# print(ramesh.salary)
# ramesh.increase()  # Even if we are calling increase method with class object then it sends "self" parameter
#                     # to the methods which it is calling.
# print(ramesh.salary)



# to see all instances of object

# print(ramesh.__dict__)  

# ramesh.domain = "Developer"  # To add any new instance of variable

# print(ramesh.__dict__)


# To see instance or vaiables of class but not methods we use class with __dict__

# print(Employee.__dict__)