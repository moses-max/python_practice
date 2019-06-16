lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!

class_list = [lloyd, alice, tyler]

def average(numbers):
  total = 0
  #print total
  total= sum(numbers)
  #print total
  total= float(total)
  #print total
  total = total / len(numbers)
  #print total
  return total

def get_average(student):
  homework = average(student["homework"]) * 0.10
  quizzes = average(student["quizzes"]) * 0.30
  tests = average(student["tests"]) * 0.60
  return homework + quizzes + tests

print get_average(lloyd)
print get_average(alice)
print get_average(tyler)


def get_letter_grade(score):
  if score >= 90:
  	return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

print get_letter_grade(get_average(lloyd))

def get_class_average(class_list):
  results = []
  for student in students:
   results.append(get_average(student))
  return average(results)

students = [lloyd, alice, tyler]
print get_class_average(students)
print get_letter_grade(get_class_average(students))