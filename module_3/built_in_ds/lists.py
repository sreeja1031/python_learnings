jon_snow = ["Jon Snow", "Winterfell", 30]
print(jon_snow)

# Indexing
print(jon_snow[0])

# Length
print(len(jon_snow))

print(jon_snow[2])
jon_snow[2] += 3
print(jon_snow[2])

num_seq = range(0, 10) 
print(type(num_seq)) # A sequence from 0 to 9
num_list = (list(num_seq))  # The list() method casts the sequence into a list
print(num_list)

world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners[0][1])

part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
part_A += part_B
print(part_A)

part_A = [1, 2, 3, 4, 5]
part_B = [5, 6, 7, 8, 9, 10]
part_A.extend(part_B)
print(part_A)

num_list = []  # Empty list
num_list.append(1)
num_list.append(2)
num_list.append(3)
print(num_list)

num_list = [1, 2, 3, 5, 6]
num_list.insert(3, 4)  # Inserting 4 at the 3rd index. 5 and 6 shifted ahead
print(num_list)

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
last_house = houses.pop()
print(last_house)
print(houses)
houses.remove("Ravenclaw")
print(houses)

num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list[2:5])
print(num_list[0::2])

cities = ["London", "Paris", "Los Angeles", "Beirut"]
print(cities.index("Los Angeles"))  # It is at the 2nd index
print("London" in cities)
print("Moscow" not in cities)

num_list = [20, 40, 10, 50.4, 30, 100, 5]
num_list.sort()
print(num_list)

