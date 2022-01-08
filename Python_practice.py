# counties = ["Arapahoe", "Denver", "Jefferson"]
# first_item = counties[0]
# print(first_item)
# print(len(counties))
# counties.insert(2, "Deantown")
# print(counties)
# counties.remove("Deantown")
# print(counties)
# counties.insert(1, 'El Paso')
# print(counties)
# # counties.remove(0)
# # counties[2] = "Denver"
# # counties[1] = "Jefferson"
# # counties.append("Arapahoe")
# # print(counties)
# counties.remove("Arapahoe")
# print(counties)
# counties[2] = "Denver"
# counties

# my_tuple = ("Derp", "Shit", "Ass")
# print(len(my_tuple))
# print(type(my_tuple))

# Creating a dictionary
# counties_dict = {}
# print(type(counties_dict))
# # OR my_dictionary = dict()
# counties_dict["Arapahoe"] = 422829
# counties_dict["Denver"] = 463353
# counties_dict["Jefferson"] = 432438
# print(counties_dict)

voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})

print(voting_data)
voting_data.append({"county": "El Paso", "registered_voters": 461149})
