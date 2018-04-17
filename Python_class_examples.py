#FIRST class example (basic class)
class Employes_first:
    n=0
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employes_first.n+=1
    def show(self):
        return(self.name,self.age,self.salary)

# first class objects generator
Emp1 = Employes_first('Peter',35,70000)
Emp2 = Employes_first('John',41,90000)
Emp3 = Employes_first('Tony',41,90000)

data = [Emp1.show(), Emp2.show(), Emp3.show()]
print('FIRST CLASS EXAMPLE OUTPUT:')
print(data)
print("Number of employes: ",Employes_first.n)
print()


#SECOND class example (inheritance && override)
class Employes_second:
    n=0
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employes_second.n+=1
    def show(self):
        return(self.name,self.age,self.salary)


class Developers(Employes_second):
    dev_n = 0
    def __init__(self,name,age,salary,language):
        super().__init__(name,age,salary)
        self.language = language
        Developers.dev_n+=1
    def show(self):
        return(self.name,self.age,self.salary,self.language)

# second class objects generator
Dev1 = Developers('Kevin',35,70000,'Python')
Dev2 = Developers('Martin',41,67000,'Java')
Dev3 = Developers('Joanna',41,930000,'C++')
Dev4 = Developers('Sara',41,85000,'Perl')

data = [Dev1.show(), Dev2.show(), Dev3.show(), Dev4.show()]
print('SECOND CLASS EXAMPLE OUTPUT:')
print(data)
print("Number of developers: ",Developers.n)
print()


#THIRD class example (inheritance && override without __init__ child class)
class Employes_third:
    n=0
    def __init__(self,name,surname,age,salary):
        self.name = name
        self.age = age
        self.surname = surname
        self.salary = salary
        Employes_third.n+=1
    def show(self):
        return(self.name,self.surname,self.age,self.salary)


class Employes_extension(Employes_third):
    def show(self):
        return(self.name + '.' + self.surname + '@' + 'company.com')

# third class objects generator
Emp1_third = Employes_extension('Robert','Smith',41,70000)
Emp2_third = Employes_extension('Jeff','Doe',28,90000)
Emp3_third = Employes_extension('Joey','Ramone',37,90000)
Emp4_third = Employes_extension('Tony','Soprano',37,90000)
Emp5_third = Employes_extension('Jessica','Goodwood',37,90000)

data = [Emp1_third.show(), Emp2_third.show(), Emp3_third.show(),
        Emp4_third.show(), Emp5_third.show()]
print('THIRD CLASS EXAMPLE OUTPUT')
print(data)
print("Number of employes: ",Employes_extension.n)
print()


#FOURTH class example (inheritance && call parent class method (*args,**kwargs))
class Employes_forth:
    n=0
    def __init__(self,name,surname,age,salary):
        self.name = name
        self.age = age
        self.surname = surname
        self.salary = salary
        Employes_forth.n+=1
    def show_E(self,flag):
        if flag == True:
            print('Employe name is:',self.name,', Employe surname is: ', self.surname)
        elif flag == False:
            print('Employe age is: ',self.age, ', Employe salary is: ', self.salary)


class Employes_extension_args_kwargs(Employes_forth):
    def show_c(self,*args,**kwargs):
        if self.age > 29:
            super(Employes_extension_args_kwargs,self).show_E(*args,**kwargs)
        else:
            print('Employee is under 29 years old')

# fourth class objects generator
Emp1_forth = Employes_extension_args_kwargs('Robert','Smith',41,70000)
Emp2_forth = Employes_extension_args_kwargs('Jeff','Doe',27,90000)
Emp3_forth = Employes_extension_args_kwargs('Joey','Ramone',37,90000)
Emp4_forth = Employes_extension_args_kwargs('Tonny','Soprano',25,90000)
Emp5_forth = Employes_extension_args_kwargs('Jessica','Goodwood',37,90000)

print('FORTH CLASS EXAMPLE OUTPUT')
Emp1_forth.show_c(True)
Emp2_forth.show_c(False)
Emp3_forth.show_c(True)
Emp4_forth.show_c(False)
Emp5_forth.show_c(True)
print("Number of employes: ",Employes_extension_args_kwargs.n)
