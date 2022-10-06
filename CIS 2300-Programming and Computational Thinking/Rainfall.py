#Creating an empty list
ListRainfall=[]
#Creating a range 
for e in range (1,13):78
    ListRainfall.append(int(input("Please enter rainfall for month "+str(e)+":")))
    
print("The Total Rainfall:",sum(ListRainfall))
print("The Average Rainfall:",sum(ListRainfall)/len(ListRainfall))
print("The Highest Rainfall:",max(ListRainfall))
print("The Lowest Rainfall",min(ListRainfall))
