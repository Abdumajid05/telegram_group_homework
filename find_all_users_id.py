from read_data import read_data
import json 

def find_all_users_id(data: dict)->list:
    l=[]
    for i in data["messages"]:
        if "from_id" in i:
            l.append(i["from_id"])
        else:
            l.append(i["actor_id"])
    return l

print(find_all_users_id(read_data('result.json')))


    