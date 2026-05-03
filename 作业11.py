phrase=input("please input a phrase :").title()
words=phrase.split()
acronym=""
for each in words:
    acronym+=each[0]
print("the acronym is :%s."%acronym)
