class fraction(object):
    def __init__(self,numer,denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + '/'+str(self.denom)
    def get_Numer(self):
        return self.numer
    def get_Denom(self):
        return self.denom
    def __add__(self,other):
        numerNew = other.getDenom()*self.getNumer()+other.getNumer()*self.get_Denom()
        denomNew = other.getDenom()*self.getDenom
        return fraction(numerNew,denomNew)
    def __sub__(self,other):
        numerNew = other.getDenom()*self.getNumer()- other.getNumer()*self.get_Denom()
        denomNew = other.getDenom()*self.getDenom
        return fraction(numerNew,denomNew)
    def convert(self):
        return self.getNumer()/self.get_Denom

class intSet(object):
    def __init__(self):
        self.vals = []
    def insert(self,e):
        if not e in self.vals:
            self.vals.append(e)
    def member(self):
        return e in self.vals
    def remove(self,e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + 'not found')
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result+str(e)+','
        return '{'+result[:-1] +'}'

