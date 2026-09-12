#task:
#create a dictionary using codegnan portal as example. keys:Exams,Mock Interview,course-completion percentage,rank,attendence streak,exam streak

codegnan_balaji={
    "Daily-exams":("mon","Tue","wed","thu","fri","sat"),
    "weekly-exams":{"week-1":85,"week-2":53.35,"week-3":81.67,"week-4":88.33},
    "mocks":{'mock-1':3,'mock-2':7},
    "subjects":['python','sql','data analytics','powerbi','excel'],
    "course-completion-percentage":56.8,
    "attendence-streak":25,
    "daily-exam-streak":21
}

print(codegnan_balaji["Daily-exams"])
print(codegnan_balaji["weekly-exams"])
print(codegnan_balaji["mocks"])
print(codegnan_balaji["subjects"])
print(codegnan_balaji["course-completion-percentage"])
print(codegnan_balaji["attendence-streak"])
print(codegnan_balaji["daily-exam-streak"])

#calculating weekly avg without revealing actual values
sum=0
count_of_weekly_exams=list()
for i in codegnan_balaji["weekly-exams"].keys():
    sum=sum+codegnan_balaji["weekly-exams"][i]
    count_of_weekly_exams.append(codegnan_balaji["weekly-exams"][i])
avg_of_weekly_exams=sum/len(count_of_weekly_exams)
print(f"avgerage weekly percentage: {avg_of_weekly_exams}")