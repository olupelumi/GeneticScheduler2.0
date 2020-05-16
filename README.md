# GeneticScheduler
### Problem:

Every week in the summer, the personel manager at Coffeehouse( a local coffeshop at my University where I previously worked) has to go through survey information on a spreadsheet where 14 or more people put their preferences (e.g "I want this shift", "I'm neutral about this shift", " I'd prefer not to work this shift", "I cannot work this shift"). She then takes the next two hours to try and come up with a schedule that fulfills as many of people's preferences as possible. 

### My approach:

When first thinking about this problem, I knew that there had to be a way to automate this with technology. I had just learned about genetic algorithms in my Program Design class and I felt that approach would be a great fit for this problem because there is no deterministic right answer(final schedule). All that is needed was something that was good enough. There is also some inherent notion of scoring or fitness in the problem as each person has preferences for shifts and the personel manager tried to find a schedule with as many people as possible getting their preference

Below I have my log and how I decided to design everything and why

## Design:

### Preprocessing:

**Creating a score Matrix:**

Need a scoring matrix where the rows are the names, the columns are each shift and at each entry is the preference score that the person gave for that shift.

### Schedule Agent Class:

Each schedule created will be represented as so:

[ {"Jay", "Gbenga", "Olumide"}, {"May", "Olumide", "Jay"}...] 

where the index of the array represents the shift and each set represents the people in each shift.

**Making a random schedule:**

I need to create a random schedule in the aforementioned format using some json data.

I have a list of names so I can just place three people in each shift with equal probability. And I do it immediately. 

**Calculating Fitness:**

Taking a relatively simple approach to calculating fitness. I'm going to look at the person at a certain shift and see what their preference score for that shift is ( 1-4) and then sum up all the preference scores at each shift. 

The more 4s and 3s I get, the higher the score will be. 

Will use the scoring matrix to get the preference scores.

## Possible Improvements:

###Project still in progress
