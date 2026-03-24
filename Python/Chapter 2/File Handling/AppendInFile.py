path = "D:\\EduNet\\NSTI_Indore25_26\\Python\\Chapter 2\\File Handling\\AppededInFile.txt"

File = open(path, 'a')

update = "\nAt 5 we Departed to Homes"

File.write(update)
print(type(File))
File.close()
