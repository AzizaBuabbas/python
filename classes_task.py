from datetime import datetime

class Employee:
	 def __init__(self , name , age , salary ,employment_date):
	 	self.name = name
	 	self.age = age 
	 	self.salary = salary 
	 	self.employment_date = employment_date/

	 	def get_working_years(self):
	 		today = datetime.now()
	 		current_year = today.year 
	 		return current_year - int(self.employment_date)

class Manager(Employee):
	def __init__ (self , name , age , salary , employment_date , bonus_percentage):
		super(self , name , age , salary , employment_date)
		self.bonus_percentage = bonus_percentage

	def get_bonus(self):
		return float(self.bonus_percentage) * int(self.salary)

employment_list = []
Manager_list = []

print("\tWelcome to HR Pro 2019")
print("\tChoose an action to do:")
print("\t\t1. Show Employees")
print("\t\t2. Show Managers")
print("\t\t3. Add an Employee")
print("\t\t4. Add a Manager")
print("\t\t5. Exit")
print()


choice = input ("What would you like to do ?")

while choice != "5":
	if choice == "1":
		print("-----------------")
		print("Employees")
		for q in employment_list:
			print("Name: %s, Age: %s , salary: %s , working years: %s " % (q.name, q.age , q.salary, q.get_working_years()))

	print("___________________________")

elif choice=="2":
	print("_________________")
	print("Managers")
	for q in employment_list:
		print("Name: %s , Age: %s , salary: %s, Working years: %s , Bonus: %s"% (q.name, q.age , q.salary, q.get_working_years(), q.get_bonus()))

		print("---------------------------")
	elif choice == "3":
		print("-----------------")
		name = input("Name:")
		age = input ("Age:")
		salary = input("salary:")
		employment_year = input ("Employment Year:")

		Employee = Employee(name . age , salary , employment_year)

		employment_list.append (Employee)






