#class that represents a scedule
#from Survey import names
import json
import random
class Schedule:
    def __init__(self, numShifts, nameList):
        self.fitness = -1 #value before 
        self.nameList = nameList;
        #The actual schedule information
        self.numShifts = numShifts
        self.content = [set(random.sample(self.nameList, k = 2)) for _ in range(self.numShifts)] #WIll be an array of sets

    def __str__(self):
        return ("numshifts: " + str(self.numShifts) + " content: " + str(self.content))
    
    def compute_fitness(self):
        """
        Requires:
        Nothing

        Effects:
        Calculates the fitness of the current schedule. 
        """
        #This is gonna be where the bulk of my thinking is
        pass

    def to_json(self):
        #may be used later. Not sure yet.
        pass

    def get_content(self):
        return self.content
    
    def get_fitness(self):
        return self.fitness