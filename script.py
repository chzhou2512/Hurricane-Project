# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
updated_damages = []
#if last letter of the string is B, convert by B - similar for M, otherwise same

def damage_control(record):
  conversion = {"M": 1000000,
              "B": 1000000000}
  new_damages = []
  for occurrence in record:
   if occurrence == "Damages not recorded":
    new_damages.append(occurrence)
   elif occurrence[-1] == "M":
    new_damages.append((float(occurrence.strip("M")))*conversion["M"])
   else:
    new_damages.append((float(occurrence.strip("B")))*conversion["B"])
  return new_damages

updated_damages = damage_control(damages)
#print(updated_damages)

def hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricane_dictionary = {}
  for i in range(len(names)):
    hurricane_dictionary.update({names[i]: {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damages[i], "Death": deaths[i]}})
  return hurricane_dictionary

hurricanes = hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurricanes)


# # 3
# # Organizing by Year


def hurricane_dictionary_by_year(hurricanes):
  hurricane_dictionary_years = {}
  for occurrence in hurricanes:
    current_year = hurricanes[occurrence]["Year"]
    current_occurrence = hurricanes[occurrence]
    if current_year not in hurricane_dictionary_years:
      hurricane_dictionary_years[current_year] = [current_occurrence]
    else:
      hurricane_dictionary_years[current_year].append(current_occurrence)
  return hurricane_dictionary_years   
    
test = hurricane_dictionary_by_year(hurricanes)
#print(test)


# # create a new dictionary of hurricanes with year and key

# # 4
# # Counting Damaged Areas

# # create dictionary of areas to store the number of hurricanes involved in
def how_often_areas_are_damaged(hurricanes):
  area_damage_count = {}
  for occurrence in hurricanes:
    areas_damaged = hurricanes[occurrence]["Areas Affected"]
    for individual_place in areas_damaged: 
      if individual_place not in area_damage_count:
        area_damage_count[individual_place] = 1
      else:
         area_damage_count[individual_place] += 1
  return area_damage_count

total_areas_damaged = how_often_areas_are_damaged(hurricanes)
#print(total_areas_damaged)


 # 5 
# # Calculating Maximum Hurricane Count

# # find most frequently affected area and the number of hurricanes involved in

def max_hurricane_count(total_areas_damaged):
  total_count = list(total_areas_damaged.values())
  for area, area_count in total_areas_damaged.items():
    if area_count == max(total_count):
      return area
  

most_affected_area = max_hurricane_count(total_areas_damaged)
#print(most_affected_area)


# # 6
# # Calculating the Deadliest Hurricane

# # find highest mortality hurricane and the number of deaths
#print(hurricanes)
def greatest_number_of_deaths(hurricanes):
  max_mortality_cane = 'Cuba I'
  max_mortality = 0
  for occurrence in hurricanes:
    if hurricanes[occurrence]['Death'] > max_mortality:
      max_mortality_cane = occurrence
      max_mortality = hurricanes[occurrence]['Death']
  return max_mortality_cane, max_mortality
  

max_deaths = greatest_number_of_deaths(hurricanes)
#print(max_deaths)
#print(hurricanes)
# # 7
# # Rating Hurricanes by Mortality
# # categorize hurricanes in new dictionary with mortality severity as key
def rate_by_mortality(hurricanes):
  mortality_scale_dict = {0:[], 1:[], 2:[], 3:[], 4:[]}
  mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
  for occurrence in hurricanes:
    if hurricanes[occurrence]["Death"] == 0:
      mortality_scale_dict[0].append(hurricanes[occurrence]["Name"])
    elif hurricanes[occurrence]["Death"] > 0 and hurricanes[occurrence]["Death"] <= 100:
      mortality_scale_dict[1].append(hurricanes[occurrence]["Name"])
    elif hurricanes[occurrence]["Death"] > 100 and hurricanes[occurrence]["Death"] <= 500:
      mortality_scale_dict[2].append(hurricanes[occurrence]["Name"])
    elif hurricanes[occurrence]["Death"] > 500 and hurricanes[occurrence]["Death"] <= 1000:
      mortality_scale_dict[3].append(hurricanes[occurrence]["Name"])
    else:
      mortality_scale_dict[4].append(hurricanes[occurrence]["Name"])  
  return mortality_scale_dict

mortality_scale = rate_by_mortality(hurricanes)
#print(mortality_scale)

#print(hurricanes)

# # 8 Calculating Hurricane Maximum Damage

# # find highest damage inducing hurricane and its total cost
def greatest_damage(hurricanes):
  max_damage_occurrence = 'Cuba I'
  max_damage = 0
  for occurrence in hurricanes:
    cost_of_damage = hurricanes[occurrence]["Damage"]
    if cost_of_damage == 'Damages not recorded':
      pass
    elif cost_of_damage > max_damage:
      max_damage_occurrence = hurricanes[occurrence]['Name']
      max_damage += hurricanes[occurrence]['Damage']
  return max_damage_occurrence, max_damage

hurricane_with_greatest_damage = greatest_damage(hurricanes)
#print(hurricane_with_greatest_damage)


# # 9
# # Rating Hurricanes by Damage
# # #damage_scale = {0: 0,
# #                 1: 100000000,
# #                 2: 1000000000,
# #                 3: 10000000000,
# #                 4: 50000000000}
  
# # categorize hurricanes in new dictionary with damage severity as key
#print(hurricanes)

def rate_hurricanes_by_damage(hurricanes):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  hurricanes_by_damage_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for occurrence in hurricanes:
    damage_done = hurricanes[occurrence]['Damage']
    if damage_done == 'Damages not recorded':
      pass
    elif damage_done == damage_scale[0]:
      hurricanes_by_damage_dict[0].append(hurricanes[occurrence]['Name'])
    elif damage_done > damage_scale[0] and damage_done <= damage_scale[1]:
      hurricanes_by_damage_dict[1].append(hurricanes[occurrence]['Name'])
    elif damage_done > damage_scale[1] and damage_done <= damage_scale[2]:
      hurricanes_by_damage_dict[2].append(hurricanes[occurrence]['Name'])
    elif damage_done > damage_scale[2] and damage_done <= damage_scale[3]:
      hurricanes_by_damage_dict[3].append(hurricanes[occurrence]['Name'])
    elif damage_done > damage_scale[3] and damage_done <= damage_scale[4]:
      hurricanes_by_damage_dict[4].append(hurricanes[occurrence]['Name'])
    else:
      hurricanes_by_damage_dict[5].append(hurricanes[occurrence]['Name'])
  return hurricanes_by_damage_dict

hurricanes_damage_scale = rate_hurricanes_by_damage(hurricanes)
print(hurricanes_damage_scale)


