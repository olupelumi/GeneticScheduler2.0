#Survey.java but in python

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