#################################################################################################################################
#                                                                                                                               #
# Add polymorphism to your parent and child classes (subclasses) by adding __str__ functions.                                   #
#    The __str__ function should print the parent attributes as well as the unique child attributes.                            #
#                                                                                                                               #
# The makeNoise() function of the Animal class will need to be overridden in each subclass.                                     #
#    The makeNoise function will need to print the sound the animal makes to the screen.                                        #
#                                                                                                                               #
# All instantiated Animal objects should be stored in the Zoo list.                                                             #
#   Traverse the Zoo list using a loop and have each animal polymorphically print its attributes and call the makeNoise function# 
#                                                                                                                               #
# Be sure to use comments for both structure of the program and documentation of the code.                                      #
#                                                                                                                               #
#################################################################################################################################

class Animal():                                                                                                                 # Creates a parent class for all animals
    def __init__(self, animalType, age, color):                                                                                 # Initialize variables
        self.__animalType = animalType
        self.__age = age
        self.__color = color
    def __str__(self):                                                                                                          # A function to quickly call object attributes.
        print(('Animal Type: ' + self.get_animalType()),'\t', ('Age: ' + self.get_age()),'\t', ('Color: ' + self.get_color()), end='\t')
        return('')
    def set_animalType(self, animalType):                                                                                       # set animalType
        self.__animalType = animalType
        return
    def set_age(self, age):                                                                                                     # set Age
        self.__age = age
        return
    def set_color(self, color):                                                                                                 # set Color
        self.__color = color
        return
    def get_animalType(self):                                                                                                   # get Animal Type
        return self.__animalType
    def get_age(self):                                                                                                          # get Age
        return self.__age
    def get_color(self):                                                                                                        # get Color
        return self.__color
    def makeNoise(self):                                                                                                        # Prints Animal Noises
        print('Random Animal Noise')
        return
    
class Chicken(Animal):                                                                                                          # Creates a child class to animals for chickens
    def __init__ (self, animalType, age, color, featherSize, wattleSize, layEggs):                                              # initialize variables specific to chickens class
        Animal.__init__(self, animalType, age, color)
        self.__featherSize = featherSize
        self.__wattleSize = wattleSize
        self.__layEggs = layEggs
    def __str__(self):                                                                                                          # A function to quickly call chicken object attributes.
        print(('Feather Size: ' + self.get_featherSize()),'\t', ('Wattle Size: ' + self.get_wattleSize()),'\t', ('Lay Eggs: ' + self.get_layEggs()))
    def set_featherSize(self, featherSize):                                                                                     # set featherSize
        self.__featherSize = featherSize
        return
    def set_wattleSize(self, wattleSize):                                                                                       # set wattleSize
        self.__wattleSize = wattleSize
        return
    def set_layEggs(self, layEggs):                                                                                             # set layEggs
        self.__layEggs = layEggs
        return
    def get_featherSize(self):                                                                                                  # get featherSize
        return self.__featherSize
    def get_wattleSize(self):                                                                                                   # get wattleSize
        return self.__wattleSize
    def get_layEggs(self):                                                                                                      # get layEggs
        return self.__layEggs
    def makeNoise(self):                                                                                                        # Prints Chicken Noise
        print('Bawk')
        return

class Turtle(Animal):                                                                                                           # Creates a child class to animals for Turtles
    def __init__(self, animalType, age, color, shellShape, livesIn, limbType):                                                  # initializes variables specific to turtles class
        Animal.__init__(self, animalType, age, color)
        self.__shellShape = shellShape
        self.__livesIn = livesIn
        self.__limbType = limbType
    def __str__(self):                                                                                                          # A function to quickly call turtles object attributes
        print(('Shell Shape: ' + self.get_shellShape()),'\t', ('Lives On: ' + self.get_livesIn()),'\t', ('Type of Limbs: ' + self.get_limbType()))
    def set_shellShape(self, shellShape):                                                                                       # set shellShape
        self.__shellShape = shellShape
        return
    def set_livesIn(self, livesIn):                                                                                             # set livesIn
        self.__livesIn = livesIn
        return
    def set_limbType(self, limbType):                                                                                           # set limbType
        self.__limbType = limbType
        return
    def get_shellShape(self):                                                                                                   # get shellShape
        return self.__shellShape
    def get_livesIn(self):                                                                                                      # get livesIn
        return self.__livesIn
    def get_limbType(self):                                                                                                     # get limbType
        return self.__limbType
    def makeNoise(self):                                                                                                        # Prints Animal Noises
        print('Growl')
        return

class Cat(Animal):                                                                                                              # Creates a child class to Animals for Cats
    def __init__(self, animalType, age, color, furType, isLapCat, origin):                                                      # initiates variables specific to cats class
        Animal.__init__(self, animalType, age, color)
        self.__furType = furType
        self.__isLapCat = isLapCat
        self.__origin = origin
    def __str__(self):                                                                                                          # A function to quickly call cat object attributes
        print(('Type of Fur: ' + self.get_furType()),'\t', ('Is a Lap Cat: ' + self.get_isLapCat()),'\t', ('Origin: ' + self.get_origin()))
    def set_furType(self, furType):                                                                                             # set furType
        self.__furType = furType
        return
    def set_isLapCat(self, isLapCat):                                                                                           # set isLapCat
        self.__isLapCat = isLapCat
        return
    def set_origin(self, origin):                                                                                               # set origin
        self.__origin = origin
        return
    def get_furType(self):                                                                                                      # get furType
        return self.__furType
    def get_isLapCat(self):                                                                                                     # get isLapCat
        return self.__isLapCat
    def get_origin(self):                                                                                                       # get origin
        return self.__origin
    def makeNoise(self):                                                                                                        # Prints Animal Noises
        print('Meow')
        return
        
def main():                                                                                                                     # Main function
    zoo = []                                                                                                                    # make a blank list called zoo
    chicken1 = Chicken('Chicken', '3', 'White', 'Small' , 'Short', 'Yes')                                                       # create an object that is Chicken
    zoo.append(chicken1)                                                                                                        # add the object to the zoo list
    chicken2 = Chicken('Rooster', '4', 'Blue', 'Large' , 'Long', 'No')                                                          # create an object that is Chicken
    zoo.append(chicken2)                                                                                                        # add the object to the zoo list
    turtle1 = Turtle('SeaTurtle', '6', 'Brown', 'Soft' , 'Water', 'Soft and Spiked')                                            # create an object that is Turtle
    zoo.append(turtle1)                                                                                                         # add the object to the zoo list
    turtle2 = Turtle('Tortoise', '25', 'Green', 'Hard Dome' , 'Land', 'Stiff and Bent')                                         # create an object that is Turtle
    zoo.append(turtle2)                                                                                                         # add the object to the zoo list
    cat1 = Cat('Sphynx', '34', 'Grey', 'No Fur' , 'Yes', 'Canada')                                                              # create an object that is Cat
    zoo.append(cat1)                                                                                                            # add the object to the zoo list
    cat2 = Cat('Siberian', '11', 'Orange', 'Long Fur' , 'No', 'Norway')                                                         # create an object that is Cat
    zoo.append(cat2)                                                                                                            # add the object to the zoo list
    for i in zoo:                                                                                                               # For every item in the zoo list
        Animal.__str__(i)                                                                                                       # call the __str__ function from the Animal class
        i.__str__()                                                                                                             # call the __str__ function from the subclass 'i' corrisponds to
        i.makeNoise()                                                                                                           # calls the makeNoise function from the correct object
        if isinstance(i, Chicken):                                                                                              # if i is a chicken
            print('I am a Chicken')                                                                                             # print 'I am a Chicken'
        elif isinstance(i, Turtle):                                                                                             # if i is a turtle
            print('I am a Turtle')                                                                                              # print 'I am a Turtle'
        elif isinstance(i, Cat):                                                                                                # if i is a cat
            print('I am a Cat')                                                                                                 # print 'I am a Cat'
        print('')                                                                                                               # print a blank line to seperate each object for readability
    input('Press ENTER to Close')
main()                                                                                                                          # call the main function
