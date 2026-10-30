gradebook = {
    "Math": [94, 87, 90],
    "English": [86, 99, 70],
    "Science": [82, 91, 97],
    "History": [94, 91, 87],
}
 
 def add_grade(subject, grade):
    if subject not in gradebook:
        gradebook[subject] = []
    gradebook[subject].append(grade)

def get_average(subject):
    grades = gradebook[subject]
    return sum(grades) / len(grades)
    

def print_average(subject):
    if subject in gradebook:
        average = round(get_average(subject), 2)
        print(subject, "average:", average)
    else:
        print("That subject is not in the gradebook.")
 
 
def print_grades(subject):
    if subject in gradebook:
        print(subject, "grades:", gradebook[subject])
    else:
        print("That subject is not in the gradebook.")
 
 
# Prints every subject's average, plus the best and worst subjects
def print_all_averages():
    best_subject = ""
    worst_subject = ""
    best_average = 0
    worst_average = 100
 
    for subject in gradebook:
        average = get_average(subject)
        print(subject + ":", round(average, 2))
 
        # Keep track of the highest and lowest averages so far
        if average > best_average:
            best_average = average
            best_subject = subject
        if average < worst_average:
            worst_average = average
            worst_subject = subject
 
    print()
    print("best subject", best_subject)
    print("worst subject", worst_subject)
 
 def grade_to_points(average):
    if average >= 92.5:
        return 4.0
    elif average >= 89.5:
        return 3.7
    elif average >= 79.5:
        return 3.0
    elif average >= 69.5:
        return 2.0
    elif average >= 65.0:
        return 1.0
    else:
        return 0.0
 
def get_GPA():
    total_points = 0
    for subject in gradebook:
        total_points = total_points + grade_to_points(get_average(subject))
    return total_points / len(gradebook)
 
 
