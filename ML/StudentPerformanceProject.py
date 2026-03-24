# Hours Studied
# Previous Scores
# Extracurricular Activities
# Sleep Hours
# Sample Question Papers Practiced

import pickle

print("\tWelcome to Student Performance Prediction")

StudyHour = int(input("Enter Hours Studied :: "))
PrevScore = int(input("Enter Previous Score :: "))
ExCurr = int(input("Do Extra Curricular Activities :: "))
SleepingHours = int(input("Enter Sleeping Hours :: "))
SamplePaper = int(input("How Many Question Paper Solved ::"))

print(StudyHour, PrevScore, ExCurr, SleepingHours, SamplePaper)


with open("D:\\EduNet\\NSTI_Indore25_26\\ML\\Model\\StudentPerformanceModel.pkl",'rb') as file:
    model = pickle.load(file)
    
prediction = model.predict([[StudyHour, PrevScore, ExCurr, SleepingHours, SamplePaper]])[0]

print("Your Performance Score is :: ", prediction )
