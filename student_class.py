class Student:
  def __init__(self, name, student_id, grades):
    self.name = name
    self.student_id = student_id
    self.grades = grades


  def add_grade(self, grade):
    self.grades.append(grade)

  def calculate_average(self):
    average = sum(self.grades) / len(self.grades)
    print(f"The average grade is {average:.2f}")
    return average
  
  def display_info(self):
    print(f"Here are all the grades {self.grades}")
    average = self.calculate_average()
    print(f"Here is the average: {average:.2f}")