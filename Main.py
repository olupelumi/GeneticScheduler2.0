#Where I'll be creating a json form survey information using a genetic algorithm
import ScheduleAgent
import Population
import pandas as pd
import json
import csv
# mockSched = ScheduleAgent.Schedule(10)
# #print(mockSched)
# print(mockSched.fitness)
# print(mockSched.compute_fitness())

def write_to_csv(json_name, csv_name):
    df = pd.read_json (json_name)
    df.to_csv (csv_name, index = True)
    

#How many agents do you want in a population
population_num = 11

#How many generations
generation_num = 100

mutation_rate = 0.4

num_shift = 20

sched_score_threshold = (num_shift * 2 * 4) - 15

#Initializing the first population of agents
curr_pop = Population.Population(population_num, num_shift)
for gen in range(generation_num):

    print("curr_generation " + str(gen))
    best_agent1 = curr_pop.select_agents()[0]
    best_agent2 = curr_pop.select_agents()[1]

   # If we've gotten a schedule that's good enough
    if (best_agent1.fitness >= sched_score_threshold) :
        write_to_csv("schedule.json", "sched.csv")
        break

    if (best_agent2.fitness >= sched_score_threshold):
        write_to_csv("schedule.json", "sched.csv")
        break

        
    #creates a new population of agents
    new_pop = curr_pop.make_child_population(mutation_rate)

    #updating the population
    curr_pop = new_pop

