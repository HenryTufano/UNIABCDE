from person import Person
class Student(Person):
   
   def __init__(self,name,email,phone,ar,course):
      self.ar=ar
      self.course=course
      super().__init__(name,phone,email)

   def Show_info(self,name,email,phone,ar,course):
         if course==1:
            course="Engenharia"
         elif course ==2:
            course="Direito"
         elif course==3:
            course="pedagogia"
         self.aluno= ("Nome: "+name+"\nTelefone: "+str(phone)+"\nEmail: "+email+"\nRA: "+str(ar)+"\ncurso: "+str(course)+"\n")
         return self.aluno
        
   def monthly_payment(self,course,name):
      self.name=name
      self.course=course
      if self.course ==1:
         cur="a mensalidade do "+name+" é de R$2000,00"
      elif self.course==2:
        cur="a mensalidade do "+name+" é de R$1500,00"
      elif self.course==3:
         cur="a mensalidade do "+name+" é de R$500,00"
      return cur

