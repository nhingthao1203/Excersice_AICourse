class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def count_doctor(self):
        count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.people.sort(key=lambda x: x.yob)

    def compute_average(self):
        sum_yob = 0
        count = 0
        for person in self.people:
            if isinstance(person, Teacher):
                sum_yob += person.yob
                count += 1
        return sum_yob / count

    def describe(self):
        print(f"Ward: {self.name}")
        for person in self.people:
            person.describe()


class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(f"Student: {self.name}, yob: {self.yob}, grade: {self.grade}")


class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(
            f"Teacher: {self.name}, yob: {self.yob}, subject: {self.subject}")


class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(
            f"Doctor: {self.name}, yob: {self.yob}, specialist: {self.specialist}")


# Output:
# 2(a)
# Example 1:
student1 = Student(name=" studentA ", yob=2010, grade="7")
student1.describe()

# Example 2:
teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
teacher1.describe()

# Example 3:
doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
doctor1.describe()

# 2(b)
print()
teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
ward1 = Ward(name=" Ward1 ")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

# 2(c)
print()
print(f"\n Number of doctors : {ward1 . count_doctor()}")

# 2(d)
print()
print("\n After sorting Age of Ward1 people ")
ward1.sort_age()
ward1.describe()

# 2(e)
print(f"\n Average year of birth ( teachers ): {ward1.compute_average()}")
