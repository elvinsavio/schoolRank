import json


with open('school.json', 'r') as openfile:
  
    #  Reading from json file
    li = json.load(openfile)

idx = 1
rank_list = {}

while (len(li) != 0):
    max_val = 0
    max_key = []

    for i in li:
        if li[i] >= max_val:
            max_val = li[i]
            max_key.append(i)
    
    for key in max_key:
        li.pop(key)
        rank_list[key] = {
            "val":max_val,
            "rank": idx
        }
    idx+=1

with open('rankedschools.json', 'w') as openfile:
    openfile.write(json.dumps(rank_list))
