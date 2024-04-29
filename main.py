


print("This calculator can convert feet into yards and yards into feet.")

conv = input("Are you converting 1. feet to yards or 2. yards to feet? Enter a 1 or 2 ") 
if conv == "1":
  print("okay")
  feet = int(input("How much feet? "))
  yards = str(input(feet/3))


  
else:
  yard = int(input("how many yards? "))
  if conv == "2":
    print ("okay")
    feet1 = str(input(yard*3))