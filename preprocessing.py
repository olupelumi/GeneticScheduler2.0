import pandas
import json

# Figure out how to get this python code to work in intellij
surveydf = pandas.read_excel('SummerAvailabilityWeek7.xlsx')

#Editing thhe dataframe so worker's preferences can be in terms of numerical categories. 
#The idea is that this will be useful later for computing fitness in the genetic algorithm
surveydf_changed = surveydf.mask(cond = surveydf == "I CANNOT work this shift",other = 1)
surveydf_changed = surveydf_changed.mask(cond = surveydf_changed == "I'd PREFER NOT to work this shift",other = 2)
surveydf_changed = surveydf_changed.mask(cond = surveydf_changed == "I'm NEUTRAL about this shift",other=3)
surveydf_changed = surveydf_changed.mask(cond = surveydf_changed == "I WANT this shift",other = 4)
surveydf_changed = surveydf_changed.mask(cond = surveydf_changed == "I WANT to work this shift",other = 4)

#coverting the pandas dataframe to json
tempsurvey_json = surveydf_changed.to_json(orient='records')
parsed_survey_json = json.loads(tempsurvey_json)#parsing the json

#print(json.dumps(parsed_survey_json, sort_keys=True, indent=4))

#Now I want to write this json to a file.
survey_json={}
survey_json["survey data"]=parsed_survey_json

#writing the json to a file
with open('survey_data.json', 'w') as outfile:
    json.dump(survey_json, outfile)

 
#print('Excel Sheet to JSON:\n', json.dumps(survey_json, sort_keys=True, indent=4))