import json

dict ={
    "name":'Happy',
    "Age":22,
    "course":'computer'
}

with open("json_example.json","w") as file:
    json.dump(dict,file,indent=4)     
