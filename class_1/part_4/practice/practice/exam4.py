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

class UG(MITPerson):
    def __init__(self,name,classYear):
        MITPerson.__init__(self,name)
        self.year = classYear
    def getClass(self):
        return self.year
    def speak(self,utterance):
        return MITPerson.speak(self,"Dude,"+utterance)

class Grad(MITPerson):
    pass

def isStudent(obj):
    return isinstance(obj,UG) or isinstance(obj,Grad)
p1 = Person('Mark Zuckerberg')
p1.setBirthday(5,14,84)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,83)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,55)
p4 = Person('Andrew Gates')
p5 = Person ('Steve Wozniak')

personList = [p1,p2,p3,p4,p5]

for e in personList:
    print(e)
personList.sort()
for e in personList:
    print(e)