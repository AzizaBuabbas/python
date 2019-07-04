skills = ["coding" , "Juggling","Python", "horseback riding"]
cv = {}

name = input("Name:")
cv ["name"] = name 

age = input ("Age:")
cv ["age"] = int(age)

experience = input("How many years of experience do you have?")
cv["experience"] = experience 

cv["skills"]= []

print ("Skills:")
print("1. %s" % skills [0])
print("2. %s" % skills [1])
print("3. %s" % skills [2])
print("4. %s" % skills [3])

skill1 = input ("choose a skill from above:")
cv["skills"].append(skills[int(skill1)-1])

skill2 = input ("choose another skill from above:")
cv["skills"].append(skills[int(skill2)-1])

if int(cv["age"]) >= 18 and int(cv["age"]) < 45 and (cv["skills"][0] == skills[2] or cv["skills"][1]== skills[2]):
	print("you have been accepted, %s "% cv["name"])
else:
	print("loser.")