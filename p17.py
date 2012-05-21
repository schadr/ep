import sys

words = ['one','two','three','four','five','six','seven','eight','nine']
teens = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
hundred = "hundred"
thousand = 'thousand'

# 21124

s = len('ten')*10
for w in words:
  s += len(w)*9*10+len(w)*100

for t in teens:
  s += len(t) * 10

for t in tens:
  s += len(t)*10*10

s += len(hundred)*9*100
s += len('and')*9*99

s += len(words[0]) + len(thousand)

print(s)
