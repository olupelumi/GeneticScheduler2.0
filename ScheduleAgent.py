#class that represents a scedule
#from Survey import names
import json
import random
import Survey
from collections import defaultdict
import json

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
        return ("numshifts: {}, content: {}, fitness: {}".format(self.numShifts, self.content, self.fitness))
    
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

    def to_json(self, json_file_nm):
        """
        Requires:
        json_file_nm, file name for the json file to be written

        Effects:
        converts the content of this schedule object into a json and that json is written to a file
        """
        #may be used later. Not sure yet.
        json_dict = defaultdict(dict)

        for idx, shift in enumerate(self.content):
            person1_dict = json_dict["person 1"]
            person2_dict = json_dict["person 2"]

            person1_dict[Schedule.id_to_shift[idx]] = list(shift)[0] 
            person2_dict[Schedule.id_to_shift[idx]] = list(shift)[1] 
        
        not_default_dict =  dict(json_dict)
        print("type2: {}".format(type(not_default_dict)))

        #writing created json to a json file.
        with open(json_file_nm, 'w') as outfile:
            json.dump(not_default_dict, outfile)
            
        #returns json dict in dictionary form and not default dict form
        return not_default_dict

