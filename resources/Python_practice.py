

counties = ["Arapahoe", "Denver", "Jefferson"]
my_list = list(counties)
print(counties)

counties.append("El Paso")
print(counties)

counties.insert(2, "El Paso")
print(counties)

counties.remove("El Paso")
print(counties)

counties[2] = "El Paso"



counties_tuple = ("Arapahoe", "Denver", "Jefferson")
len(counties_tuple)

my_dictionary = dict()
counties_dict = {'Arapahoe' : 422829, 'Denver' : 463353, 'Jefferson' : 432438}

voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters" : 422829})
voting_data.append({"county": "Denver", "registered_voters" : 463353})
voting_data.append({"county": "Jefferson", "registered_voters" : 432438})


counties = ["Arapahoe", "Denver", "Jefferson"]
if counties [1] == 'Denver':
    print((counties[1]))

    counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

    for county in counties: 
       print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)    

for i in range(len(counties)):
    print(counties[i])
 


for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
for county_dict in voting_data:
    print(county_dict['county'])

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)



