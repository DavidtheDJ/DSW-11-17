#David Justice
#11-17-16
#Animal Sim Practice

import random

class Animal:
    """A generic animal"""

    #Constructor
    def __init__(self,growth_rate,food_need,water_need,name):
        #set the attributes with an intial value

        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Baby"
        self._type = "Generic"
        self._name = ""

        #the above attributes are prefixed with an underscore to indicate
        #that they should not be accessed directly from outwith the class

    def needs(self):
        #return a dictionary containing the light and water needs
        return {"food need":self._food_need, "water need":self._water_need}

    #method to report the provide information about the current state of the crop
    
    def report(self):
        #return a dicionary containing the type, status, growth and days growing
        return {'type':self._type,'status':self._status,'days growing':self._days_growing,'weight':self._weight,'name':self._name}
    
    def _update_status(self):
        if self._weight > 1500:
            self._status = "Fat Adult"
            self._weight = self._weight + 200
        elif self._weight > 1000:
            self._status = "Adult"
            self._weight = self._weight + 1000
        elif self._weight > 400:
            self._status = "Fat Baby"
            self._weight = self._weight + 400
        elif self._weight > 60:
            self._status = "Baby"
            self._weight = self._weight + 200
        elif self._weight >= 0:
            self._status = "New Born"
            self._weight = self._weight + 63

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update the status
        self._update_status()

def auto_grow(animal, days):
    #grow the crop
    for days in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(light,water)

def manual_grow(animal):
    #get the light and eater values from the user
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a food value (1-10): "))
            if 1 <= light <=10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid - please enter a value between 1 and 10")

    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1,10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid - please enter a value between 1 and 10")

        #grow the animal
        animal.grow(light,water)


def main():
    #instanitate the class
    new_animal = Animal(1,6,5,"")
    #test to see whether code works or not
    print(new_animal.needs())
    print(new_animal.report())
    manual_grow(new_animal)
    print(new_animal.report())

if __name__ == "__main__":
    main()

