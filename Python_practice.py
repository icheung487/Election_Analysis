counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if "el paso" in counties: 
    print ("el paso is in the list of counties")
else:
    print("el paso is not the list of counties")
if "Araphahoe" in counties and "el paso" in counties:
    print ("Arapahoe and el paso are in the list of counties")
else:
    print("arapahoe or el paso is not in the list of counties")
print(counties)
if "arapahoe" in counties and "el paso" not in counties: 
    print ("Only Arapahoe is in the list of countries")
else:
    print("arapahoe is in the list of counties and el paso is not in the list")
numbers = [0,1,2,3,4]
for num in numbers:
    print(num)
for num in range(5):
    print(num)
for i in range(len(counties)):
    print (counties[i])
for i in (counties):
    print(i)
counties_dict ={"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
print(counties_dict)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict: 
    print(counties_dict[county])
for county,voters in counties_dict.items():
    print(county,voters)
for county,voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
voting_data =[{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver","registered_voters":463353},{"county":"Jefferson","registered_voters":432438}]
for county_dict in voting_data:
     print(county_dict)
for i in range(len(voting_data)):
    print(voting_data[i])
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
for county_dict in voting_data:
    print(county_dict['registered_voters'])
for county_dict in voting_data:
    print(county_dict['county'])
car = {"brand":"Ford", "model":"Mustang", "year":1964}
x = car.items()
print (x)
candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes} number of votes."
    f" The total number of votes in the election was {total_votes}."
    F"You received {candidate_votes /  total_votes * 100:.2f} % of the total votes.")
print(message_to_candidate)


















