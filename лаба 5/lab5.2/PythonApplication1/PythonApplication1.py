import re

text = input()

sentences = re.split(r'\s*(?<=[.?!])\s+', text)

sentences = [s.strip() for s in sentences if s.strip()]


for s in sentences:
    print(s)
    
print("предложение в тексте: ", len(sentences))
