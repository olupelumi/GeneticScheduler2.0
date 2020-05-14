#class that represents a scedule
#from Survey import names
import json
import random
class Schedule:
    def __init__(self, numShifts):
        self.fitness = None
        #The actual schedule information
        self.numShifts = numShifts
        self.content = [] #WIll be an array of sets
        
    def from_json(self, nameList):
        """
        Requires:
        nameList is a list of names as strings

        Effect:
        generates a random schedule based on the names
        """
        #need to make a random schedule to place in content
        for shift_num in range(self.numShifts):
            self.content.append(set(random.sample(nameList, k = 2)))


    def __str__(self):
        return ("numshifts: " + str(self.numShifts) + " content: " + str(self.content))

    def to_json(self):
        pass
