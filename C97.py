name= 'Kyra'
print(name)

age= int(input("Enter your age: "))
#int = integer

if(age<= 13):
    print("Less than 13")

elif(age>13):
    print("Greater than 13")

else:
    print("Enter a number please!")


words= input("Please enter a sentence- ")
wordcount= 1

countries=['India','Pakistan', 'China', 'America']

for country in countries:
    print(country)
for i in words:
    if(i== ' '):
        wordcount=wordcount+1



print("The total number of words :- ")
print(wordcount)

age=13

while(age<18):
    print(age)
    age+=1