# import re

# pattern =r"\d+"
# text ="Do you have a charger for my 2 iphones each one of 240W"

# match = re.findall(pattern,text)
# print(match)


import re

pattern = r"\d{4}-\d{2}-\d{2}"

text = "on 2023-05-12 the trip will begin."

match = re.findall(pattern, text)
print(match)