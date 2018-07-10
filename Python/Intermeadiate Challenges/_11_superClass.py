import datetime


class User:
    '''Class dedicated to users of a University'''

    def __init__(self, name, surname, dob, gender):
        self.fname = name
        self.sname = surname
        self.dob = str(dob)                               # ddmmyyyy
        self.gender = gender

        def fullName(name, surname): return name.strip().title() + ' ' + surname.strip().title()
        self.fullName = fullName(self.fname, self.sname)
        self.email = '{}{}{}@University.edu'.format(
            self.sname.strip().lower()[0:3], self.fname.strip().lower()[0:3], str(datetime.date.today().year)[2:4])

    def userAge(self):
        '''Returns the age in years of a User.'''
        now = datetime.date.today()
        yyyy = int(self.dob[4:8])
        mm = int(self.dob[2:4])
        dd = int(self.dob[0:2])
        DOB = datetime.date(yyyy, mm, dd)
        age = int((now - DOB).days / 365)
        return age

    def display(self):
        print('Fullname: {}'.format(self.fullName))
        print('Age: {}'.format(User.userAge(self)))
        print('Gender: {}'.format(self.gender))
        print('Email: {}'.format(self.email))


u1 = User('   DagaN', 'oRTOn  ', 17042001, 'male')
u2 = User(' SHaWn      ', '  ortON ', 22081975, 'male')

User.display(u2)
