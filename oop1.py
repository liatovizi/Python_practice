class Customer():
    def set_name(self, new_name):
        self.name = new_name
    def identify(self):
        print('I am a customer ' + self.name)
    def set_salary(self, new_salary):
        self.salary = new_salary

    def give_raise(self, amount):
        try:
            self.salary = self.salary + amount
        except:
            print('He is a cat')

cust = Customer()
cust.set_name('Lia')
cust.identify()
cust.set_salary(5000)
print(cust.salary)
cust.give_raise(1000)
print(cust.salary)

cust2 = Customer()
cust2.set_name('Nexi')
cust2.identify()
cust2.set_salary("he doesn't need salary")
cust2.give_raise(1000)
print(cust2.salary)

from datetime import datetime

class Empleado:
    def __init__(self, nombre, salario=0):
        self.nombre = nombre
        if salario >= 0:
            self.salario = salario
        else:
            self.salario = 0
            print("Invalido")
        self.hiredate = datetime.today()

    def give_raise2(self, amount2):
        self.salario += amount2

    def monthly_salary2(self):
        return self.salario / 12



emp = Empleado("Eli", -1000)
print(emp.nombre)
print(emp.salario)
print(emp.hiredate)

#####
class Emp:
    MIN_SAL = 30000
    def __init__(self, name, salary):
        self.name = name
        if salary >= Emp.MIN_SAL:
            self.salary = salary
        else:
            self.salary = Emp.MIN_SAL
@classmethod
def from_file(cls, filename):
    with open(filename, 'r') as f:
        name = f.readline()
    return cls(name)
