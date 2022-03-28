def find_averg_marks(marks):
    sum_of_marks=sum(marks)
    total_subjects=len(marks)
    avg_marks=sum_of_marks/total_subjects
    return avg_marks
marks=[34,64,78,25,13,65]
avg_marks=find_averg_marks(marks)
print(avg_marks)

def computer_grade(avg):
    if avg_marks>=80:
        grade="a"
    elif avg_marks>=60:
        grade="b"
    elif avg_marks>=50:
        grade="c"
    else:
        grade="f"
    return grade
grade=computer_grade(avg_marks)
print("your grade is",grade)

