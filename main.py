from student_class import Student

name = input("Enter student name: ")
student_id = input("Enter student ID: ")

grades = []

student = Student(name, student_id, grades)

while True: 
  print("""Welcome to UTS.
  1. Add grade
  2. Display student info 
  3. Exit""")

  choice = int(input("Enter your option (1-3): "))

  if choice == 1:
    grade = float(input("Enter the grade: "))
    student.add_grade(grade)

  elif choice == 2:
    student.display_info()

  elif choice == 3:
    break

  else: 
    print("Invalid choice, try again.")