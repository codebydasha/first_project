'''class Employee:
        name = ""
        id = ""

def lisaa():
    name = input("Anna työntekijän nimi (0 lopetus):")

def main():

    tyontekijat = []
    for i in range(0, "name"):
        lisaa()
        tyontekijat.append(Employee)
    print(id, tyontekijat)


class Person:
    age: int = 5
    name: str = 'Nelli'

p1 = Person()
p1.hair_color = 'black'


print(getattr(Computer, 'sdf', str(math.pi)))
pprint.p'''

class SalaryEmployee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary

class PayrollSystem: #tulostusfunktio
    def calculate_payroll(employees):
        counter = 0
        for i in employees:
            print("Palkkalaskelma")
            print("==============")
            print(f"Henkilölle: {counter+1} -", i.name)
            print("- Maksetaan:", i.calculate_salary(), end='\n')
            print(end='\n')
            counter = counter + 1

#pääohjelma
employees = []
salarylist = []

def tyontekijat(): #hakufunktio
    while True:
        name = input("Anna työntekijän nimi: (0 lopetus): ")
        if name == "0":
            break
        monthly_salary = int(input("Anna kuukausipalkka: "))
        employees.append(SalaryEmployee(name, monthly_salary))
    return employees

if __name__ == "__main__":
    employees = tyontekijat()
    PayrollSystem.calculate_payroll(employees)






