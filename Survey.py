#Survey.java but in python
import json
import re
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

#shifts in a sorted manner
shift_list = [
'Monday (6/24) [7:30 am - 8:55 am]',
'Monday (6/24) [8:55 am - 9:55 am]',
'Monday (6/24) [9:55 am - 10:55 am]',
'Monday (6/24) [10:55 am - 11:55 am]',
'Monday (6/24) [11:55 am - 12:55 pm]',
'Monday (6/24) [12:55 pm - 1:55 pm]',
'Monday (6/24) [1:55 pm - 2:55 pm]',
'Monday (6/24) [2:55 pm - 3:55 pm]',
'Monday (6/24) [3:55 pm - 4:55 pm]',
'Monday (6/24) [4:55 pm - close]',
'Tuesday (6/25) [7:30 am - 8:55 am]',
'Tuesday (6/25) [8:55 am - 9:55 am]',
'Tuesday (6/25) [9:55 am - 10:55 am]',
'Tuesday (6/25) [10:55 am - 11:55 am]',
'Tuesday (6/25) [11:55 am - 12:55 pm]',
'Tuesday (6/25) [12:55 pm - 1:55 pm]',
'Tuesday (6/25) [1:55 pm - 2:55 pm]',
'Tuesday (6/25) [2:55 pm - 3:55 pm]',
'Tuesday (6/25) [3:55 pm - 4:55 pm]',
'Tuesday (6/25) [4:55 pm - close]',
'Wednesday (6/26) [7:30 am - 8:55 am]',
'Wednesday (6/26) [8:55 am - 9:55 am]',
'Wednesday (6/26) [9:55 am - 10:55 am]',
'Wednesday (6/26) [10:55 am - 11:55 am]',
'Wednesday (6/26) [11:55 am - 12:55 pm]',
'Wednesday (6/26) [12:55 pm - 1:55 pm]',
'Wednesday (6/26) [1:55 pm - 2:55 pm]',
'Wednesday (6/26) [2:55 pm - 3:55 pm]',
'Wednesday (6/26) [3:55 pm - 4:55 pm]',
'Wednesday (6/26) [4:55 pm - close]',
'Thursday (6/27) [7:30 am - 8:55 am]',
'Thursday (6/27) [8:55 am - 9:55 am]',
'Thursday (6/27) [9:55 am - 10:55 am]',
'Thursday (6/27) [10:55 am - 11:55 am]',
'Thursday (6/27) [11:55 am - 12:55 pm]',
'Thursday (6/27) [12:55 pm - 1:55 pm]',
'Thursday (6/27) [1:55 pm - 2:55 pm]',
'Thursday (6/27) [2:55 pm - 3:55 pm]',
'Thursday (6/27) [3:55 pm - 4:55 pm]',
'Thursday (6/27) [4:55 pm - close]',
'Friday (6/28) [7:30 am - 8:55 am]',
'Friday (6/28) [8:55 am - 9:55 am]',
'Friday (6/28) [9:55 am - 10:55 am]',
'Friday (6/28) [10:55 am - 11:55 am]',
'Friday (6/28) [11:55 am - 12:55 pm]',
'Friday (6/28) [12:55 pm - 1:55 pm]',
'Friday (6/28) [1:55 pm - 2:55 pm]',
'Friday (6/28) [2:55 pm - 3:55 pm]',
'Friday (6/28) [3:55 pm - 4:55 pm]',
'Friday (6/28) [4:55 pm - close]'
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
cnt = 0
def compute_score_matx(jdata):
    """
    Requires:
    jdata is the survey preference information in json format

    Effects:
    Returns a dictionary representing a score matrix, telling me the score at amy name,shift pairing
    """
    score_mat = {}
    survey_lst = jdata["survey data"]
    #iterating over each preference information
    for name_pref_dict in survey_lst:
        name_val = name_pref_dict["Name"]
        score_mat[name_val] = {}
        for shift, pref_score in name_pref_dict.items():
            #here I need to get the index of the shift
            #Need to error check now
            #Thinking I could use regular expressions since the strings representing the shifts are of the same pattern. 
            if re.match(r"[a-zA-Z]+\s\(\d[\d]?/\d[\d]?\)\s\[\d[\d]?:\d[\d]?[\s]?[ap]m[\s]?-[\s]?(\d[\d]?:\d[\d]?[\s]?[ap]m|close)\]", shift):
                score_mat[name_val][shift] = pref_score
    return score_mat


#opening and reading the jsonfile
jsonfile = open("survey_data.json")
#turning json data into a dictionary
json_data = json.load(jsonfile)
#print(json_data)

print(compute_score_matx(json_data))


