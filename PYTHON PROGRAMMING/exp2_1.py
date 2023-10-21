n=int(input("ENTER NUMBER OF STUDENTS:"))
student_marks={}
for i in range(n):
    name,*line=input("ENTER STUDENTS NAME:").split()
    scores=list(map(float,line))
    student_marks[name]=scoresquery_name=input("ENTER STUDENT MARKS:")
    print()
