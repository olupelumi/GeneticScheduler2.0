#Where I'll be creating a json form survey information using a genetic algorithm
import ScheduleAgent
import Population

# mockSched = ScheduleAgent.Schedule(10)
# #print(mockSched)
# print(mockSched.fitness)
# print(mockSched.compute_fitness())


#population_num = int(input("How many agents do you want in a population(an even integer)? "))
population_num = 11

#generation_num = int(input("How many generations? "))
generation_num = 100

#mutation_rate = float(input("mutation rate(a number between 0 and 1)? "))
mutation_rate = 0.4

num_shift = 10

#Initializing the first population of agents
curr_pop = Population.Population(population_num, num_shift)
for gen in range(generation_num):

    print("curr_generation " + str(gen))
    best_agent1 = curr_pop.select_agents()[0]
    best_agent2 = curr_pop.select_agents()[1]

   # I've gotten a schedule that's good enough
    if (best_agent1.fitness >= 65) :
        print("bestagent1 got a schedule good enough")
        print(best_agent1)
        print(best_agent1.to_json("schedule.json"))
        break

    if (best_agent2.fitness >= 65):
        print("bestagent2 got a schedule good enough")
        print(best_agent2)
        print(best_agent2.to_json("schedule.json"))
        
        break

        
    #creates a new population of agents
    new_pop = curr_pop.make_child_population(mutation_rate)

    #updating the population
    curr_pop = new_pop

