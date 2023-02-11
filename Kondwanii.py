import re
firstfile = re.compile(r"Kondwani",re.I) #a regular expression to search for 'Kondwani'
firstfile_1 = open("Kon1.txt",'r')       # opening a new txt file called Kon1
Kondwani = firstfile.findall(firstfile_1.read()) #creates a list full of all the 'Kondwani's present in the Kon1 txt file
print(Kondwani)                          # testing what the outcome looked like

Kondwani_2 = open(r'result.txt','a')     #opening a new txt file called result
counter = 0                              #initializing a counter 

for i in Kondwani:
    counter +=1                           #counter the number of 'Kondwani's present in the list Kondwani

Kondwani_2.write(f'Number of Kondwani\'s is :{ counter}\n') # writes the results into the new txt file results

firstfile_1.close()
Kondwani_2.close()

