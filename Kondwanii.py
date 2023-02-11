import re
firstfile = re.compile(r"Kondwani",re.I)
firstfile_1 = open("Kon1.txt",'r')
Kondwani = firstfile.findall(firstfile_1.read())
print(Kondwani)

Kondwani_2 = open(r'result.txt','a')
counter = 0

for i in Kondwani:
    counter +=1

Kondwani_2.write(f'Number of Kondwani\'s is :{ counter}\n')

firstfile_1.close()
Kondwani_2.close()

