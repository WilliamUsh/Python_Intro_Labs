# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers)
# numbers2 = [11,12,13,14,15,16,17,18,19,20]
# numbers += numbers2
# print(numbers)
# numbers += [21,22,23,24,25]
# print(numbers)
# numbers += "hello"
# print(numbers)

# print()
# print()

#creating a bird array
print("Lists Lab")
print()
birds = ["sparrow", "blue jay", "blue bird", "lyrebird", "mourning dove", "cardinal", "woodpecker", "peacock"]
print(birds)
print()

#Modifying
print("Changing blue bird to sparrow ")
birds[2] = "sparrow" #blue bird should become sparrow
print(birds)
print()

#Removing
print("removing objects")
birds2 = birds
del birds2[3]
print(birds2)
del birds2[4:]
print(birds2)
print()

#Append
print("Using append")
birds.append("swan")
print(birds)
birds.append(["robin", "crane"])
print(birds)
print()

#Extend
print("Using extend")
birds.extend(["kookaburra"])
print(birds)
birds.extend(["crow", "raven"])
print(birds)
print()

#Inserting
print("Inserting at certain points")
birds.insert(3, "pigeon")
print(birds)
print()

#Counting
print("Counting the number of times an element appears")
print(str(birds.count("sparrow")) + " sparrows are in the list")
print()

#Sorting
print("Using sort to rearrange the list alphabetically")
del(birds[6])
birds.sort()
print(birds)
print("Sorting in reverse alphabetical")
birds.sort(reverse=True)
print(birds)
print()

#Remove
print("Using remove to remove sparrows from the list")
birds.remove("sparrow")
birds.remove("sparrow")
print(birds)
print()
print()
print()

#Applying Your Knowledge
print("Applying Your Knowledge")
print()
my_friends = ["Rizzo", "French", "Danny", "Kenickie", "Marty", "Sandy", "Cha-Cha", "Patty", "Sonny", "Calhoun"]
print(my_friends)
#print out the length of the list
print(len(my_friends))
#print out the 4th friend's name
print(my_friends[3])
#print out the 11th friend's name (What happens?)
#print(my_friends[10])  Errors
#print out the last friend's name (Use negative indexing)
print(my_friends[-1])
#print out the 5th - 8th friend's names
print(my_friends[5:9])
#print out the last 5 names (Do not place a number in both start and stop)
print(my_friends[5:])
#print out the first 3 names (Do not place a number in both start and stop)
print(my_friends[:3])
#print out every other name, starting at the first name
print(my_friends[::2])
#print out every third name, starting at the last name going backwards to the front of the list.
print(my_friends[::-3])
#change the 8th friend's name to "Elizabeth". Print out the changed list.
my_friends[7] = "Elizabeth"
print(my_friends)
#add a new friend, Danny, to the end of the list. Print out the changed list.
my_friends.append("Danny")
print(my_friends)
#remove the 7th friend's name (They ate the last cookie in the jar). Print out the changed list.
del(my_friends[8])
#insert a new friend, Sandy, in the 3rd spot of the list. Print out the changed list.
my_friends.insert(2, "Sandy")
#print out the number of times the name Sandy appears in the list.
print(my_friends.count("Sandy"))
#sort the list to be in alphabetical order. Print out the sorted list.
my_friends.sort()
print(my_friends)