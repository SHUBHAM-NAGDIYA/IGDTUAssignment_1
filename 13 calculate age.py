#Write a program that asks the user for their birth year and calculates their age
from datetime import date

#Date of Birth
year,month,day=map(int,input("enter date of birth in equence (year,month,date)").split())

#def calculateAge(birthDate):
today = date.today()
age = today.year - year -((today.month, today.day) <(month, day))
print(age,"years")
 
