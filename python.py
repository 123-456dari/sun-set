class Parrot:

    
    name = ""
    age = 0


parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10
print(f"{parrot1.name} is {parrot1.age} years old")



# base class
class Animal:
    
    def eat(self):
        print( "I can eat!")
    
    def sleep(self):
        print("I can sleep!")

# derived class
class Dog(Animal):
    
    def bark(self):
        print("I can bark! Woof woof!!")
