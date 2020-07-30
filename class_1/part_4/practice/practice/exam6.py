import datetime

class Person(object):
    def __init__(self,name):
        """creat a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
    def getLastName(self):
        return self.LastName
    def __str__(self):
        return self.name
    def setBirthday(self,month,day,year):
        """set self's birthday to birthDate"""
        self.birthday = datetime.date(year,month,day)
    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return(datetime.date.today()-self.birthday).days
    def __lt__(self,other):
        if self.lastName == other.lastName:
            return self.name<other.name
        return self.lastName<other.lastName

class MITPerson(Person):
    nextIdNum = 0
    def __init__(self,name):
        Person.__init__(self,name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __lt__(self,other):
        return self.idNum<other.idNum
    def speak(self,utterance):
        return (self.getLastName()+' says: '+ utterance)

class Student(MITPerson):
    pass

class Grade(object):
    def __init__(self):
        self.students = []
        self.grades = {}
        self.isSorted = True
    def addStudent(self,student):
        if student in self.students:
            raise ValueError('Duplicated student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    def addGrade(self,student,grade):
        try:
            self.grades[student.getIdNum()].append(grade)
        except Keyerror:
            raise VauleError('Student not in grade book')
    def getGrades(self,student):
        try:
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise VauleError('Student not in grade book')
    def allStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]

def gradeReport(course):
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot+=g
            numGrades+=1
        try:
            average = tot/numGrades
            report.append(str(s)+'\'s mean grade is '+str(average))
        except ZeroDivisionError:
            report.append(str(s)+'has no grades')
    return '\n'.join(report)