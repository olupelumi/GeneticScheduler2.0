#Population.java but in python
import json
import random
import ScheduleAgent
import Survey
class Population:
    def __init__(self, population_numb, numShifts):
        self.num_pop = population_numb
        self.numShifts = numShifts
        self.agent_list = [ScheduleAgent.Schedule(self.numShifts) for _ in range(self.num_pop)]
    
    #setter
    def set_agent_list(self, agent_lst):
        self.agent_list = agent_lst
    
    #getter
    def get_agent_list(self):
        return self.agent_list

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
        #print(len(self.agent_list))
        sorted_agents = sorted(self.agent_list, key = lambda agent: agent.fitness, reverse = True)
        
        rand1 = random.randint(0, len(sorted_agents) - 1)
        rand2 = random.randint(0, len(sorted_agents) - 1)
        #print(rand1, rand2)
        parent1 = sorted_agents[rand1]
        parent2 = sorted_agents[rand2]

        #print("parent 1: {},\n parent 2: {}\n".format(parent1, parent2))
        return (parent1, parent2)

    def crossbreed(self, parent1, parent2):
        """
        Requires:
        two agent schedules, agent 1 and agent 2

        Effect:
        Computes a new population from crossbreeding these two agents
        Returns a new population instance created from crossbreeding
        """
        offspring_agents =[]
        for _ in range(self.num_pop//2):
            #choosing a random number between 0 and the number of shifts, exclusive
            split_idx = random.randint(0, self.numShifts)

            #One way I can crossbreed is to combine the first portions of the first parent and the end portions of the second parent. 
            #The new schedule beginning will be the beginning of the first parent and add the end of the string will be the end of the second parent and vice versa
            
            child1_content = parent1.get_content()[:split_idx] + parent2.get_content()[split_idx:self.numShifts]
            child2_content = parent2.get_content()[:split_idx] + parent1.get_content()[split_idx:self.numShifts]

            #creating the agent offspring
            child1_agent = ScheduleAgent.Schedule(self.numShifts)
            child2_agent = ScheduleAgent.Schedule(self.numShifts)
            

            #Setting the strings
            child1_agent.set_content(child1_content)
            child2_agent.set_content(child2_content)

            #append the agents
            offspring_agents.extend([child1_agent, child2_agent])
        
        #creating a new population instance
        child_pop = Population(self.num_pop, self.numShifts)

        #setting the new list of agents
        child_pop.set_agent_list(offspring_agents)

        return(child_pop)

    def mutate(self, agent):
        """
        Requires:
        agent is an instance of the StringAgent class

        Effect:
        mutates the inputted agent
        returns the mutated agent
        """
        #used because crossover doesn't always give enough diversity and one may start converging on a set of solutions
        #allows one to look at more candidates in the search space

        rand_idx = random.randint(0, self.numShifts)
        old_content = agent.get_content()
        #replacing a random shift in the schedule with a radomly generated string
        new_content = list(old_content[:rand_idx])
        new_content.append(set(random.sample(Survey.names, k = 2)))
        new_content.extend(old_content[rand_idx + 1:self.numShifts])

        #setting the newly mutated string
        agent.set_content(new_content)
        return agent

    def make_child_population(self, mutation_rate):
        """
        Requires:
        mutation_rate is a float between 0 and 1 telling us how often we want to mutate the population

        Effect:
        returns a new population from the current population
        """
        #selecting parent agents to crossbreed
        elite_agent1, elite_agent2 = self.select_agents()
        new_pop = self.crossbreed(elite_agent1, elite_agent2)

        new_pop_lst = []
        for cand_agent in new_pop.get_agent_list():
            #checking if we need to mutate
            if (random.uniform(0,1.0) <= mutation_rate):
                #then we mutate
                newag = self.mutate(cand_agent)
                new_pop_lst.append(newag)
                #print("new mutated agent: {}".format(newag))
                continue
            #else add the agent as it is
            new_pop_lst.append(cand_agent)
        
        #setting a new population list
        new_pop.set_agent_list(new_pop_lst)

        return new_pop
