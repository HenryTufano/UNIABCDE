from person import Person
import datetime
class Employer(Person):
    def __init__(self,name,phone,email,salary,sd):
        self.salary=salary
        self.sd=sd
        super().__init__(name,phone,email)
    
    def work_days(self,sd,name):
        self.name=name
        datapadrao = datetime.date(sd[0], sd[1], sd[2])
        hoje = datetime.date.today()

        if datapadrao > hoje:
            delta = datapadrao - hoje
            
        elif datapadrao <= hoje:
        
            delta = hoje - datapadrao
            
        dt="O professor "+name+" trabalha hà "+str(delta)
        
        return dt