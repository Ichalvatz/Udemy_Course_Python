#Ask the user for a list of 3 friends
# For each friend, we 'll tell the user whether they are nearby
# For each nearby friend, we 'll save their name to ' nearby _friends.txt

friends = []

friends.append(input("Gime me 1 friend: ")) 
friends.append(input("Gime me 1 friend: ")) 
friends.append(input("Gime me 1 friend: ")) 



file_peo = open('people.txt','r')
file_peo_r = file_peo.read().splitlines()
print(file_peo_r)

for friend in friends:
    if friend in file_peo_r:
        print("That friend is nearby")
        file_nea = open('nearby_friends.txt','a')
        file_nea.write(friend)
        file_nea.write('\n')
        file_nea.close()
    else:
        print("That friend is away")

file_peo.close()