name = str(input('Enter your name: '))
f_name = str(input("Enter your father's name: "))
roll_no = str(input('Enter your roll number: '))
sub_name1, sub_num1 = str(input('Enter subject 1 name: ')) , eval(input('Enter subject 1 numbers: '))
sub_name2, sub_num2 = str(input('Enter subject 2 name: ')) , eval(input('Enter subject 2 numbers: '))
sub_name3, sub_num3 = str(input('Enter subject 3 name: ')) , eval(input('Enter subject 3 numbers: '))
sub_name4, sub_num4 = str(input('Enter subject 4 name: ')) , eval(input('Enter subject 4 numbers: '))
sub_name5, sub_num5 = str(input('Enter subject 5 name: ')) , eval(input('Enter subject 5 numbers: '))

obtained_marks = sub_num1 + sub_num2 + sub_num3 + sub_num4 + sub_num5
total_marks = 500       # 100 marks for each subject
percentage = (obtained_marks/total_marks)*100
if obtained_marks != 0:
    
    if percentage <= 59:
        grade = 'F'
    if percentage >= 60:
        grade = 'D'
    if percentage >= 70:
        grade = 'C'
    if percentage >= 80:
        grade = 'B'
    if percentage >= 90:
        grade = 'A'
else:
    print('Please enter valid obtained marks')
    
print(f"\n\t\tPersonel Details:\t\t\nName: {name.title()} \nFather's name: {f_name.title()} \nRoll number: {roll_no} \n\t\tSubject Details\t\t\n")
print(f"{sub_name1.upper()}: {sub_num1}")
print(f"{sub_name2.upper()}: {sub_num2}")
print(f"{sub_name3.upper()}: {sub_num3}")
print(f"{sub_name4.upper()}: {sub_num4}")
print(f"{sub_name5.upper()}: {sub_num5}")
print(f"Obtained marks: {obtained_marks} \nTotal: {total_marks} \nGrade:{grade} \nPercentage = {round(percentage,3)}%")
