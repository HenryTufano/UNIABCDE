from employer import Employer
class Teacher(Employer):
    def __init__(self,name,phone,email,course,salary,sd):
        self.name=name
        self.phone=phone
        self.email=email
        self.course=course
        self.salary=salary
        self.sd=sd
        super().__init__(name,phone,email,salary,sd)

    def additional_health_hazard(self,salary,course,name):
        self.name=name
        if self.course ==1:
            salary=self.salary+(self.salary*0.3)
        
        elif self.course ==2:
            salary=self.salary+(self.salary*0.05)
    
        elif self.course==3:
            salary=self.salary+(self.salary*0.15)
        sar=("O salario do professor "+name+" é "+str(salary))
        return sar 
    def Show_info(self,name,phone,email,salary,course,sd):
        if course==1:
            course="Engenharia"
        elif course ==2:
            course="Direito"
        elif course==3:
            course="pedagogia"
        self.professor= ("Nome: "+name+"\nTelefone: "+str(phone)+"\nEmail: "+email+"\nSalario: "+str(salary)+"\ncurso: "+str(course)+"\nData de engresso: "+str(sd)+"\n")
        return self.professor