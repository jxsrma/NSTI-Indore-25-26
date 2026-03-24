import csv

PATH = "D:\\EduNet\\NSTI_Indore25_26\\Python\\Chapter 2\\File Handling\\Student Details.csv"

Data = [

    ["Name", "Class", "Section", "Roll"],
    ["Aditi", "AIPA", "101", 1],
    ["Anjali", "AIPA", "101", 2],
    ["Anuradha", "AIPA", "101", 3],
    ["Dakshita", "AIPA", "101", 4],
    ["Divyanshi", "AIPA", "101", 5],
    ["Isha", "AIPA", "101", 6],
]

print("Data:", Data)

with open(PATH,'w',newline='') as csvFile:
    CSVwriter = csv.writer(csvFile)
    CSVwriter.writerows(Data)
