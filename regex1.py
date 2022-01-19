import re

text = "My telephone number is 408-555-1234"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print(phone.group())

re.search(r'\d{3}-\d{3}-\d{4}',text)

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
print(results.group())
print(results.group(1))
print(results.group(2))

re.search(r"man|woman","This man was here.")
re.findall(r".at","The cat in the hat sat here.")
re.findall(r'\S+at',"The bat went splat")
re.findall(r'\d$','This ends with a number 2')
re.findall(r'^\d','1 is the loneliest number.')

phrase = "there are 3 numbers 34 inside 5 this sentence."
print(re.findall(r'[^\d]',phrase))
print(re.findall(r'[^\d]+',phrase))


test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall('[^!.? ]+',test_phrase))
clean = ' '.join(re.findall('[^!.? ]+',test_phrase))
print(clean)

text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
print(re.findall(r'[\w]+-[\w]+',text))


