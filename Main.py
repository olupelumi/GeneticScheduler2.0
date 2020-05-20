#Where I'll be creating a json form survey information using a genetic algorithm
import ScheduleAgent
import Population

mockSched = ScheduleAgent.Schedule(10)
#print(mockSched)
print(mockSched.fitness)
print(mockSched.compute_fitness())


#population_num = int(input("How many agents do you want in a population(an even integer)? "))
population_num = 10

#generation_num = int(input("How many generations? "))
generation_num = 10

#mutation_rate = float(input("mutation rate(a number between 0 and 1)? "))
mutation_rate = 0.3

num_shift = 10

# #Initializing the first population of agents
# curr_pop = Population.Population(population_num, num_shift)
# for gen in range(generation_num):
#     print("curr_generation " + str(gen))

#     #creates a new population of agents
#     new_pop = curr_pop.make_child_population(mutation_rate)

#     #updating the population
#     curr_pop = new_pop
 

