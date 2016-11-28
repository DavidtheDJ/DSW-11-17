#David Justice
#11-23-16
#Sheep Override

from New_Animals import *

class Sheep(Animal):
    """A sheep animal"""

    #construtor
    def __init__(self):
        #call the parent class constructor with default values for cow
        #growth rate = 1; light need = 2; water need = 5
        super().__init__(1,3,6,"")
        self._type = "Sheep"

    #override frow method for subclass
    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "New Born" and water > self._water_need:
                self._weight += self._growth_rate * 1.6
            elif self._status == "Baby" and water > self._water_need:
                self._weight += self._growth_rate + 1.3
            else:
                self._weight += self._growth_rate
        #increament day growing
        self._days_growing += 1
        #update the status
        self._update_status()

def main():
    #create a new potato crop
    sheep_animal = Sheep()
    print(sheep_animal.report())
    #manually grow the crop
    manual_grow(sheep_animal)
    print(sheep_animal.report())
    manual_grow(sheep_animal)
    print(sheep_animal.report())

if __name__ == "__main__":
    main()
