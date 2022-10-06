#To input the weight of your item
Weight=int(input('Enter weight of your item\n'))
#To enter shipping as Regular or Overnight
Shipping=input('Please enter the type of shipping. Regular or Overnight\n' )
#Regular is 7 dollars if the weight is less than 5.
#Regular is 14 dollars if the weight is between 5 to 9.
#Regular is 20 dollars if the weight is between 10.
#Overnight is 15 dollars if the weight is less than 5.
#Overnight is 25 dollars if the weight is between 5 to 9.
#Overnight is 40 dollars if the weight is between 10.
if Shipping=="Regular":
    if Weight<5:
        Price=7
    if Weight>5<10:
      Price=14
    if Weight >10:
      Price=20
    print("$"+str(Price))
elif Shipping=="Overnight":
    if Weight<5:
        Price=15
    if Weight>5<10:
        Price=25
    if Weight >10:
        Price=40
    print("$"+str(Price))
else:
    print("Error")
