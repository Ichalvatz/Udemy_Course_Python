# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
#The data from cvs_file.txt are like this
"""
Manchester United,Manchester,UK
Real Madrid,Madrid,Spain
Juventus,Turin,Italy
"""
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:
import json

cvs_f = open('cvs_file.txt','r')
cvs_read = cvs_f.read().strip().split('\n')
cvs_f.close()
# print(cvs_read)
cvs_li = []
for value in cvs_read:
    cvs_li.append(value.split(','))

# print(cvs_li)


# print(cvs_l)
list_to_be_dict = []
# dict.append({"club":"uk"})
# print(dict[0]["club"])

for line in cvs_li:
    list_to_be_dict.append({"club": line[0],"city": line[1],"country": line[2]})

# print(list_to_be_dict)

out_file = open("quiz14_json.txt", "w")


json.dump(list_to_be_dict, out_file)
  
out_file.close()