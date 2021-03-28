inputStr = input("Enter a string: ")
str1 =inputStr
print(str1.upper())

vowels = 'A,E,I,O,U,a,e,i,o,u'
v = vowels.split(",")
for s in v :
    inputStr = inputStr.replace(s, "@")
print(inputStr)

for ss in str1 :
    if ss not in v:
        str1 =str1.replace(ss,"%")
print((str1))






