from teacher import Teacher
from student import Student
import os
op=99
ia=0
ip=0
aluno=[]
professor=[]
sd=[]
s=[]
pa=[]
men=[]
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
while op!=0:
    op=int(input("Escolha uma das opçoes:\n 1 - Deseja cadastrar um novo estudante\n2 - Deseja cadastrar um novo Professor \n3 - Mostrar informação \n4 - Mostrar mensalidades\n5 - Mostrar dias de trabalho\n6 - Adicional de peculiaridade\n7-atalho de usuarios\n8-criar cadastro\n9-Efetuar login\nEscolha a sua opção: "))
    if op == 1:
        if ia<2:
            clear()#exatamente
            name=input('Digite o nome da pessoa :')
            phone= input("Digite o telefone: ")
            email= input("Digite o email: ")
            ar= input("Digite o numero de matricula: ")
            course= int(input("Selecione a opção do curso: \n1-Engenharia\n 2-Direito\n 3-Pedagogia"))
            if ia==0:
                a=Student(name,phone,email,ar,course) 
                
                
            elif ia==1:
                x=Student(name,phone,email,ar,course)
                
            print('-'*15)
            ia=ia+1
            
        else:
            print("Alunos maximos cadastrados")
            
    elif op == 2:
        if ip<2:
            clear()
            nome=input('Digite o nome da pessoa :')
            name="Nome:",nome,"\n"
            telefone = input("Digite o telefone: ")
            phone="Telefone:",telefone,"\n"
            mail = input("Digite o email: ")
            email="email:",mail,"\n"
            salario = int(input("Digite o numero de salario: ")  )     
            salary = "ra:",salario,"\n"
            curso= int(input("Selecione a opção do curso: \n1-Engenharia\n 2-Direito\n 3-Pedagogia: "))
            course="course:",curso,"\n"
            print("Digite o dia de ingresso: ")
            ano=int(input("digite o ano"))
            mes=int(input("digite o mes"))
            dia=int(input("digite o dia"))
            sd=[ano,mes,dia]
            ip=ip+1
            if ip==0:
                p1=Teacher(name,phone,email,course,salary,sd)
                
                
            elif ia==1:
                p2=Teacher(name,phone,email,course,salary,sd)
        else:
            print("Professores maximos cadastrados")
            
    elif op == 3:
        clear()
        opc=int(input("Digite qual opção que deseja ver :\n1- Para estudantes\n2-Para professores\nEscolhe uma opção: "))
        if opc==1:
            clear()
            print(a.Show_info(a.name,a.phone,a.email,a.ar,a.course))
            print(x.Show_info(x.name,x.phone,x.email,x.ar,x.course))
        elif opc==2:
            clear()     
            print(p1.Show_info(p1.name,p1.phone,p1.email,p1.salary,p1.course,p1.sd))
            print(p2.Show_info(p2.name,p2.phone,p2.email,p2.salary,p2.course,p2.sd))
    elif op == 4:
        clear()
        print(a.monthly_payment(a.course,a.name))
        print(x.monthly_payment(x.course,x.name))
        
    elif op == 5:
        clear()
        print(p1.work_days(p1.sd,p1.name))
        print(p2.work_days(p2.sd,p1.name))

    elif op == 6:
        clear()
        print(p1.additional_health_hazard(p1.salary,p1.course,p1.name))
        print(p2.additional_health_hazard(p2.salary,p2.course,p2.name))
    elif op==7:
        name="aluno1"
        phone = "4002-8922"
        email = "aluno1@gmail.com"
        ar = 1111111
        course= 1
        a=Student(name,phone,email,ar,course)
        ia=ia+1

        name="aluno2"
        phone = "4002-8922"
        email = "aluno2@gmail.com"
        ar = 222222
        course= 2
        x=Student(name,phone,email,ar,course)    
        ia=ia+1

        name = "professor1"
        phone = "4002-8922"
        email = "profesor1@gmail.com"
        course= 1
        salary = 20000
        ano=2012
        mes=2
        dia=15
        sd=[ano,mes,dia]
        p1=Teacher(name,phone,email,course,salary,sd)
        ip=ip+1

        name = "professor2"
        phone = "4002-8922"
        email = "profesor2@gmail.com"
        course= 2
        salary = 30000
        ano=2015
        mes=6
        dia=16
        sd=[ano,mes,dia]
        p2=Teacher(name,phone,email,course,salary,sd)
        ip=ip+1
    elif op ==8:
        login=input("Digite o Login: ")
        senha=input("Digite o Senha: ")
        fl=open('login.txt','w')
        fl.write(login)
        fl.close()
        fs=open('senha.txt','w')
        fs.write(senha)
        fs.close()
    elif op ==9:
        login=input("Digite o Login: ")
        senha=input("Digite a senha: ")
        fl=open('login.txt','r')
        with open('login.txt', 'r') as fl:
            pl_login = fl.readline()
        fs=open('senha.txt','r')
        with open('senha.txt', 'r') as fs:
            pl_senha = fs.readline()
        if login==pl_login and senha==pl_senha:
            print("Login efetuado com sucesso, Bem vindo "+login+"\n")
        else:
            print("senha incorreta ou usuario não cadastrado\n")