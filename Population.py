#Population.java but in python
import json
import random
import ScheduleAgent
class Population:
    def __init__(self, population_numb, numShifts):
        self.num_pop = population_numb
        self.numShifts = numShifts
        self.agent_list = [ScheduleAgent.Schedule(self.numShifts) for _ in range(self.num_pop)]

    def select_agents(self):
        """
        Requires:
        Nothing

        Effect:
        selects a mating pool of agents to use to mutate and crossbreed
        returns an aray of selected agents
        """
          #Chooses the top two most fit agents

        #sorting agents by their fitness
        sorted_agents = sorted(self.agent_list, key = lambda agent: agent.fitness, reverse = True)
        
        rand1 = random.randint(0, 10)
        rand2 = random.randint(0, 10)
    
        parent1 = sorted_agents[rand1]
        parent2 = sorted_agents[rand2]

        print("parent 1: {},\n parent 2: {}\n".format(parent1, parent2))
        return (parent1, parent2)

    def crossbreed(self):
        pass

    def mutate(self):
        pass

    def make_child_population(self):
        pass

    #and probably some setters and getters