path = "D:\\EduNet\\NSTI_Indore25_26\\Python\\Chapter 2\\File Handling\\AppededInFile.txt"

main_data = "" 

with open(path, 'r') as file:
    data = file.read()
    main_data = data.upper()
    print("1. Data is Uppercase")


with open(path, 'a') as file:

    main_data="\n*************New Upper Case Data*************\n" + main_data
    file.write(main_data)
    print("2. New Upper Data Appended")