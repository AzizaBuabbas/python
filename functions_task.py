from datetime import datetime 
def check_birthdate (year , month, day):
	today = datetime.now()
	birthday = datetime(year , month, day)
	if birthday > today :
		return False 
	else:
		return True 

def calculate_age(year , month , day ):
	today = datetime.now()
	birthdate = datetime(year, month, day)
	age = today - birthdate
	age_in_days = age.days

	years = int(age_in_days/365)
	age_in_days = age_in_days%365

	months = int(age_in_days/30)
	age_in_days = age_in_days%30 
	print ("you are %s years , %s months , and %s days old." % (years , months , age_in_days))


year = int(input ("Enter year of birth:"))
month = int(input ("Enter month of birth:"))
day = int(input ("Enter day of birth:"))


if check_birthdate (year , month, day) == True :
		calculate_age(year , month , day)
else :
		print ("You're a ghost!")
