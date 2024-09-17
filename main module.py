######################################### fucntion for imput of course name and credit hour #############
def inputcourseinfo(number):
    global total_c_hour    
    for i in range(number):
        courses.insert(i,input(f"Enter course {i+1} name: ").upper()) 
        while True:
            try:
                c_hour.insert(i,int(input(f"Enter {courses[i]} credit hours: ")))
            except ValueError:
                print("Credit hours are in numbers. idiot!")    
            else:
                total_c_hour += c_hour[i]
                break
        print()
#############################################################################################################
while True:
    name = input("Enter your name: ").capitalize()
    reg = int(input("enter registartion number: "))
    Dept = input("Enter department: ").capitalize()
    semester = input("Enter semester (Fall / spring): ").capitalize()
    sem_year = input("Enter sem_year: ").capitalize()

    num = int(input("In how many courses you have enrolled yourself: "))
    c_hour = []
    courses = []
    total_c_hour = 0 
    inputcourseinfo(num)
    grade_points = {
    "A": 4, "a": 4,
    "B+": 3.5, "b+": 3.5,
    "B": 3, "b": 3,
    "C+": 2.5, "c+": 2.5,
    "C": 2, "c": 2,
    "D+": 1.5, "d+": 1.5,
    "D": 1, "d": 1,
    "F": 0, "f": 0
    }
    grades = []
    total_grades = 0
    for i in range(num):
        while True:
            grades.insert(i,input(f"Enter {courses[i]} grade:  ").upper())
            if all(char.isalpha() or char == "+" for char in grades[i]):
                break
            else:
                print("please enter grade in alphabets: ")
        if grades[i] in grade_points:
            total_grades += (grade_points[grades[i]] * c_hour[i])

    GPA = total_grades/total_c_hour
    if GPA >= 3.5 :
        academic_standing = "Excellent"
    elif GPA >= 3 and GPA < 3.5 :
        academic_standing = "Good"
    elif GPA >= 2.5 and GPA < 3 :
        academic_standing = "satisfactory"
    elif GPA >=2 and GPA < 2.5 :
        academic_standing = "Not Good"
    elif GPA >=1 and GPA < 2 :
        academic_standing = "Warning"
    elif GPA < 1 :
        academic_standing = "Drop"
    print("-" * 90)
    print(f"name : {name}")
    print(f"Reg # : {reg}")
    print(f"Department: {Dept}")
    print()
    print(f"                      {semester} semester {sem_year}                 ")
    print("-"*90)
    print("     Course Name     |      Credits      |      Grade      ")
    print("-"*90)
    for i in range(num):
            print(f"{courses[i]:<20} | {c_hour[i]:^17} | {grades[i]:^15} ")
    print("-" * 90)
    print(f"                        Semester GPA: {round(GPA,2)}")
    print(f"                   Academic Standing: {academic_standing}")

####################################### file upload ###############################
    file = input("do you want to save this data: (y / n): ")
    if file == 'y' or file == "Y":
        with open("GPA.txt", 'a') as f:
            f.write("-" * 90 + "\n")
            f.write(f"Name: {name}\n")
            f.write(f"Registration #: {reg}\n")
            f.write(f"Department: {Dept}\n")
            f.write("\n")
            f.write(f"                      {semester} Semester {sem_year}                 \n")
            f.write("-" * 90 + "\n")
            f.write("     Course Name     |      Credits      |      Grade      \n")
            f.write("-" * 90 + "\n")
            for i in range(num):
                f.write(f"{courses[i]:<20} | {c_hour[i]:^17} | {grades[i]:^15} \n")
            f.write("-" * 90 + "\n")
            f.write(f"                        Semester GPA: {round(GPA, 2)}\n")
            f.write(f"                   Academic Standing: {academic_standing}\n\n")
    else:
        pass
    again = input("do you want to calcualte again ? (y / n): ")
    if again == 'y' or again == "Y":
        continue
    elif again == 'n' or again == 'N':
        break

        