#class that represents a scedule
#from Survey import names
import json
import random
import Survey

class Schedule:
    #class variable
    #Give a name and a shift(in that order) and it will tell you the person's preference fpr that shift 
    score_matx = Survey.scoring_matrix
    id_to_shift = Survey.idx_to_shift_map
    #names of employees
    nameList = Survey.names
    def __init__(self, numShifts):
        #The actual schedule information
        self.numShifts = numShifts
        self.content = [set(random.sample(Schedule.nameList, k = 2)) for _ in range(self.numShifts)] #WIll be an array of sets
        #max fitness is numShifts*2*4
        self.fitness = self.compute_fitness()

    def __str__(self):
        return ("numshifts: " + str(self.numShifts) + " content: " + str(self.content))
    
    #setters
    def set_content(self, schedule_content):
        self.content = schedule_content

    #getters
    def get_content(self):
        return self.content

    def get_fitness(self):
        return self.fitness

    def compute_fitness(self):
        """
        Requires:
        Nothing

        Effects:
        Calculates the fitness of the current schedule. 
        """

        fitness = 0
        for idx, shift_set in enumerate(self.content):
            for person in shift_set:
                #for each person, add their preference score for their currently assigned shift in the schedule to the total fitness number
                shift_name = Schedule.id_to_shift[idx]
                fitness += Schedule.score_matx[person][shift_name]
        return fitness

    def to_json(self):
        #may be used later. Not sure yet.
        pass

