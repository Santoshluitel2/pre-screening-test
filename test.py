#pre screening test santosh luitel
from datetime import datetime
import time	
import schedule
n=int(input("How much data do you want to enter? "))
dates =[]
times =[]
date_time=[]
a=['first','second','third','fourth','fifth','sixth','seventh',
   'eighth','ninth','tenth','eleventh','twelfth','thirteenth','fourtenth','fifteenth']#could not find dict for this kind of keyword
for i in range(n):
    input_date=input("Please enter a date:")
    dates.append(input_date) 
    input_time=input("Please enter a time:")
    times.append(input_time)
    date_time.append (input_date+ "-" +input_time)
    print("\n")

print("Thank you very much. I will notify them!\n")   
current_date_time = datetime.now().strftime("%d.%m.%Y-%H:%M")
i = 0
date_time.sort()#sorted the list so it would check  for neartest date for next loop

while True:
  current_date_time = datetime.now().strftime("%d.%m.%Y-%H:%M")
  if current_date_time == date_time[i]:
    print("The "+ a[i] + " date  has been  reached! (" +current_date_time+ ")\n")
    i = i+1
  if len(date_time)<=i:#in case every date is printed
      print("Thank you ! every date is reached.")
      exit(0)
