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
 
 
