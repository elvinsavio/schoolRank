import json 
import random
import string
import sys 

random_list = {}
print(sys.argv[1])

for i in range(int(sys.argv[1])):
    random_list[''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))] = random.randint(0,100) 

jsonObj = json.dumps(random_list)

with open('school.json', 'w') as file:
    file.write(jsonObj)
     
