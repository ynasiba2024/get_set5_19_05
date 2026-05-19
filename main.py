#2-masala
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = 0
        self.set_grade(grade)

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        if 1 <= new_grade <= 5:
            self.__grade = new_grade
        else:
            print("Baho noto'g'ri")


s1 = Student("Ali", 5)

print(s1.name)
print(s1.get_grade())
