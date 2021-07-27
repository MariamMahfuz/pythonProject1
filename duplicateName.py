List = ["Zahed", " Hasan",  "Mariam", "Pushon", "Mariam", "Mahfuz", "Zahed", "Ryan"]

dupName = set()
uniqName = []
for x in List:
    if x not in dupName:
        uniqName.append(x)
        dupName.add(x)
print(dupName)
