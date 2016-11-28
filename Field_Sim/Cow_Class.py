#David Justice
#11-23-16
#Cow Override

from New_Animals import *

class Cow(Animal):
    """A cow animal"""

    #construtor
    def __init__(self):
        #call the parent class constructor with default values for cow
        #growth rate = 1; light need = 2; water need = 5
        super().__init__(1,3,6,"")
        self._type = "Cow"

    #override frow method for subclass
    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "New Born" and water > self._water_need:
                self._weight += self._growth_rate * 1.5
            elif self._status == "Baby" and water > self._water_need:
                self._weight += self._growth_rate + 1.25
            else:
                self._weight += self._growth_rate
        #increament day growing
        self._days_growing += 1
        #update the status
        self._update_status()

def main():
    #create a new potato crop
    cow_animal = Cow()
    print(cow_animal.report())
    #manually grow the crop
    manual_grow(cow_animal)
    print(cow_animal.report())
    manual_grow(cow_animal)
    print(cow_animal.report())

if __name__ == "__main__":
    main()
