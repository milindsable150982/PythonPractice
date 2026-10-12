#Strings

firstname = "Milind"
lastname = "Sable"
print(f"Hello World {firstname} {lastname}")


#List

my_List = ["Milind", "Ashok", "Rao", "Sable"]
print(my_List)
print(my_List[0:2])

#boolean
isTrue = True
print(type(isTrue))
print(1 > 2 or 2 != 3)


#if...else
if 1==1:
  print("this is false")
elif (1==2):
   print("this is true") 
else:
   print("This is neither true or false")

grade = 75
if(grade >=90):
  print("grade A")
elif(grade >=80 and grade <=89):
  print("grade B")
if(grade >=70 and grade <=79):
  print("grade C")
if(grade >=60 and grade <=69):
  print("grade D")
if(grade <=59):
  print("you are fail")

  #Loop

workingDays = ["Monday", "Tuesday", "Wensday", "Thursday", "Friday"]

for day in workingDays:
    print(day)

i = 0

while i<5:
  if i == 2: 
     break
  i += 1
  print(i)


     