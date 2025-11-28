names = ["Aditi", "Aman", "Simran", "Saurabh", "Riya",
         "Imli", "Ishi", "Ishaani", "Reema", "Ramar"]

filtered = []

for name in names:
    if name[0].lower() == name[-1]:
        filtered.append(name)
print(filtered)

dictName = {}
for name in filtered:
    count = 0
    for nameCheck in filtered:
        if nameCheck[0] == name[0]:
            count+=1
    dictName[name[0]] = count

print(dictName)
