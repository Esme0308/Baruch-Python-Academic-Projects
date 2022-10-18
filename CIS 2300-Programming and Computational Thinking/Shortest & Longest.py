longest=''
shortest=''
print('Hello! After you enter 10 words we will see the longest and shorest word!f')
#Range of 10 Words 
for e in range(10):
    w=input("Enter word "+str(e+1)+":")
    if e==0:
        longest=w 
        shortest=w
    if len(w)>len(longest):
        longest=w
    if len(w)<len(shortest):
        shortest=w
        
print("Longest word is:",longest)
print("Shortest word is:",shortest)
