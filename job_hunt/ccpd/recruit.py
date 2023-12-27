import re

content=""
with open('ccpd/url.txt', 'r') as file:
    content = file.read()
    
pattern=re.compile(r'https?://\S+')    
matches = pattern.findall(content)
matches=set(matches)
with open('output.txt', 'w') as file:
    for match in matches:
        file.write(match)
