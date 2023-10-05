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

# write your update damages function here:
def update_damages(damages):
    updated_damages = []
    for damage in damages:
      if damage == 'Damages not recorded':
        updated_damages.append(damage)
      if damage[-1] == 'B':
        updated_damages.append(float(damage[:-1])*1000000000)
      if damage[-1] == 'M':
        updated_damages.append(float(damage[:-1])*10000000)  
    return updated_damages

updated_damages_list = update_damages(damages)
print("\nThe updated damages list:\n", updated_damages_list)

#Newly updated damages without string values
def updated_damages_new(damage):
  new_damages = []
  for i in damage:
    if i == 'Damages not recorded':
      i = float(0)
    new_damages.append(i)
  return new_damages

new_damages_list = updated_damages_new(updated_damages_list)
print("\nDamages list without string values: \n", new_damages_list)

# write your construct hurricane dictionary function here:
def hurricane(name, month, year, sus_winds, affected_areas, damage, death):
  records_of_hurricanes = {}
  for n, m, y, w, a, da, de in zip(name, month, year, sus_winds, affected_areas, damage, death):
    records_of_hurricanes.update({n:{'Name':n,'Month':m, 'Year':y, 'Max Sustained Wind':w, 'Areas Affected': a, 'Damage': da, 'Deaths': de}})
  return records_of_hurricanes

hurricane_record_name = hurricane(names, months, years, max_sustained_winds, areas_affected, new_damages_list, deaths)
print("\nHurricane records based on name:\n", hurricane_record_name)




# write your construct hurricane by year dictionary function here:
def hurricane_y(name, month, year, sus_winds, affected_areas, damage, death):
  records_of_hurricanes = {}
  for n, m, y, w, a, da, de in zip(name, month, year, sus_winds, affected_areas, damage, death):
    records_of_hurricanes.update({y:{'Name':n,'Month':m, 'Year':y, 'Max Sustained Wind':w, 'Areas Affected': a, 'Damage': da, 'Deaths': de}})
  return records_of_hurricanes

hurricane_record_year = hurricane_y(names, months, years, max_sustained_winds, areas_affected, new_damages_list, deaths)
print("\nHurricane records based on year:\n", hurricane_record_year)



# write your count affected areas function here:
def no_of_times(affected_areas):
  lst = []
  dic = {}
  for area in affected_areas:
    for i in area:
      lst.append(i)
  for i in lst:
    dic.update({i:lst.count(i)})
  return dic


# write your find most affected area function here:
def most_affected_area(area):
  h_af = sorted(area.items(), key=lambda item: item[1], reverse=True)
  return h_af[0]



# write your greatest number of deaths function here:
def max_deaths(names, deaths):
  empty = {}
  for i, j in zip(names, deaths):
    empty.update({i:j})
  max_death = sorted(empty.items(), key=lambda item: item[1], reverse=True)
  return max_death[0]



# write your catgeorize by mortality function here:
def mortality_scale():
  hurricanes_by_mortality = {1: [], 2: [], 3: [], 4: [], 5: []}
  empty = {}
  for i, j in zip(names, deaths):
    empty.update({i:j})
  for i, j in empty.items():
    if j > 0 and j <= 100:
      hurricanes_by_mortality[1].append(i)
    if j > 100 and j <= 500:
       hurricanes_by_mortality[2].append(i)
    if j > 500 and j <= 1000:
       hurricanes_by_mortality[3].append(i)
    if j > 1000 and j <= 10000:
       hurricanes_by_mortality[4].append(i)
    if j > 10000:
       hurricanes_by_mortality[5].append(i)
  return hurricanes_by_mortality



# write your greatest damage function here:
def greatest_damage(name, damage):
  emp = {i:j for i, j in zip(damage, name)}
  for i, j in emp.items():
    if j == 'Damages not recorded':
      emp[i] = float(0)
  d = sorted(emp.items(), key=lambda item: item[1], reverse=True)
  return d[0]



# write your catgeorize by damage function here:
def damage_scale():
  d_scale = hurricanes_by_mortality = {1: [], 2: [], 3: [], 4: [], 5: []}
  empty = {}
  for i, j in zip(names, new_damages_list):
    empty.update({i:j})
  for i, j in empty.items():
    if j > 0 and j <= 100000000:
      d_scale[1].append(i)
    if j > 100000000 and j <= 1000000000:
      d_scale[2].append(i)
    if j > 1000000000 and j <= 10000000000:
      d_scale[3].append(i)
    if j > 10000000000 and j <= 50000000000:
      d_scale[4].append(i)
    if j > 50000000000:
      d_scale[5].append(i)
  return d_scale

print('Wow what a piece of code')