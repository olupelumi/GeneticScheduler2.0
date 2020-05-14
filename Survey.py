#Survey.java but in python
import json

'''
 * Survey Data structure to represent the information coming from the inputted survey need the list
 * of names preference information as a mapping of a mapping(name to day/time to the number they
 * ranked that shift).
 *
 * <p>The way the surbey json is structured is that it is a an array of json objects
 *
 * <p>To be honest I'm thinking about this now and perhaps I want to also create a name class with
 * the person's specific preference but that also may be unneccessarry. I think I need to do more
 * thinking about my overall design of the project, starting at a high level at the main code
 * functionality
 *
 * <p>Also I think I should change how the "schedulePreference" data structure looks like. I'm
 * thinking it should be a Hashmap<String,Hashmap<String, Integer>> where the outer key is the name
 * of an employee and the inner value is a dictionary of a bunch of information about the
 * preferences and such of the employee.
 '''

def process_survey(jdata):
    pass

def get_names(jdata):
    """
    will be a set of names probably. We'll see what I need
    """
    pass

with open("survey_data.txt") as jsonfile:
    #json_data information
    json_data = json.load(jsonfile)
#print(json_data)

#shifts in a sorted manner
shift_list = [
'Monday (6/24) [7:30am-8:55am]',
'Monday (6/24) [8:55am-9:55am]',
'Monday (6/24) [9:55am-10:55am]',
'Monday (6/24) [10:55am-11:55am]',
'Monday (6/24) [11:55am-12:55pm]',
'Monday (6/24) [12:55 pm-1:55pm]',
'Monday (6/24) [1:55pm-2:55pm]',
'Monday (6/24) [2:55pm-3:55pm]',
'Monday (6/24) [3:55pm-4:55pm]',
'Monday (6/24) [4:55pm-close]',
'Tuesday (6/25) [7:30am-8:55am]',
'Tuesday (6/25) [8:55am-9:55am]',
'Tuesday (6/25) [9:55am-10:55am]',
'Tuesday (6/25) [10:55am-11:55am]',
'Tuesday (6/25) [11:55am-12:55pm]',
'Tuesday (6/25) [12:55pm-1:55pm]',
'Tuesday (6/25) [1:55pm-2:55pm]',
'Tuesday (6/25) [2:55pm-3:55pm]',
'Tuesday (6/25) [3:55pm- 4:55 pm]',
'Tuesday (6/25) [4:55pm-close]',
'Wednesday (6/26) [7:30am-8:55am]',
'Wednesday (6/26) [8:55am-9:55am]',
'Wednesday (6/26) [9:55am-10:55am]',
'Wednesday (6/26) [10:55am-11:55am]',
'Wednesday (6/26) [11:55am-12:55pm]',
'Wednesday (6/26) [12:55pm-1:55pm]',
'Wednesday (6/26) [1:55pm-2:55 pm]',
'Wednesday (6/26) [2:55pm-3:55 pm]',
'Wednesday (6/26) [3:55pm-4:55 pm]',
'Wednesday (6/26) [4:55pm-close]',
'Thursday (6/27) [7:30am-8:55am]',
'Thursday (6/27) [8:55am-9:55am]',
'Thursday (6/27) [9:55am-10:55am]',
'Thursday (6/27) [10:55am-11:55am]',
'Thursday (6/27) [11:55am-12:55pm]',
'Thursday (6/27) [12:55pm-1:55pm]',
'Thursday (6/27) [1:55pm-2:55pm]',
'Thursday (6/27) [2:55pm-3:55pm]',
'Thursday (6/27) [3:55pm-4:55pm]',
'Thursday (6/27) [4:55pm-close]',
'Friday (6/28) [7:30am-8:55am]',
'Friday (6/28) [8:55am-9:55am]',
'Friday (6/28) [9:55am-10:55am]',
'Friday (6/28) [10:55am-11:55am]',
'Friday (6/28) [11:55am-12:55pm]',
'Friday (6/28) [12:55pm-1:55pm]',
'Friday (6/28) [1:55pm-2:55pm]',
'Friday (6/28) [2:55pm-3:55pm]',
'Friday (6/28) [3:55pm-4:55pm]',
'Friday (6/28) [4:55pm-close]'
]

#creating my mapping of shifts
idx_to_shift_map = {idx:shift for idx, shift in enumerate(shift_list)}
shift_to_idx_map = {shift:idx for idx, shift in enumerate(shift_list)}

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