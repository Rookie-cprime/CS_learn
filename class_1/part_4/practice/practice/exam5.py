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

class Profeesor(MITPerson):
    def __init__(self,name,departemen):
        MITPerson.__init__(self,name)
        self.department = department
    def speak(self,utterance):
        new = 'in course '+ self.department +'we say '
        return MITPerson.speak(self,new+utterance)
   def lecture(self,topic):
       return self.speak('it is obivious that '+ topic)
