import re
i = "45 years"
pattern = r'^\d' #i guess
# age = (int)re.sub(pattern, '', i)
new_age = re.sub('\D', '', i)
print(new_age)
