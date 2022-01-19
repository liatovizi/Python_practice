text = "the person's phone number is 408-555-1234. call soon!"
print('phone' in text)

import re
pattern = 'phone'
print(re.search(pattern,text))

pattern = "not in text"
print(re.search(pattern,text))
match = re.search(pattern,text)
match.span()
match.start()
match.end()

matches = re.findall("phone",text)
print(matches)
len(matches)

for match in re.finditer("phone",text):
    print(match.span())
match.group()



