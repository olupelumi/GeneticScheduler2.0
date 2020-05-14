#Where I'll be creating a json form survey information using a genetic algorithm
import ScheduleAgent
import Population

mockSched = ScheduleAgent.Schedule(10)
names = ["Elizabeth Hergert",
"Alyson",
"Adriana Amaris",
"sarah gao",
"marlena fleck",
"Gabby",
"nina",
"Andrea Doan",
"Miguel",
"Laura Jabr",
"Alex",
"Morgan Seay",
"Leo"]

print(mockSched)

mockSched.from_json(names)
print(mockSched)

