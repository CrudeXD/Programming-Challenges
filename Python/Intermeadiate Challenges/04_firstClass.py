import _02_Goldbach


class Student:

    def __init__(self, fname, sname, age, sex):
        self.fname = fname
        self.sname = sname
        self.age = age
        self.sex = sex
        self.email = '{}.{}@school.edu'.format(self.sname.lower(), self.fname.lower())

    def fullName(self):
        return '{} {}'.format(self.fname, self.sname)

    def display(self):
        print("Name of Learner: " + self.fullName())
        print("Age: " + str(self.age))
        print("Email: " + self.email)
        print("Sex: " + self.sex)


stud1 = Student('Dagan', 'Orton', 17, 'male')

Student.display(stud1)
print(_02_Goldbach.gold(44))
