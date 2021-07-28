import time
import re
import shutil
import matplotlib.pyplot as plt
from tabulate import tabulate
start_time = time.time()


File=open("/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/min_proj_1/files/sample1.txt","w") # location of the directory where the text file is present

for i in range(1000000):
    File.writelines("Sample Text")

for i in range(500):
    shutil.copyfile("/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/min_proj_1/files/sample1.txt",dst=f"/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/min_proj_1/files/file{i}.txt") # copying the above opened file multiple times in the directory location

    with open(f"/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/min_proj_1/files/file{i}.txt", 'r') as inp: # reading the text files made in the directory above
        y=inp.read().upper()

    with open(f"/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/min_proj_1/files/file_out{i}.txt", 'a') as out: #writing in the text files the uppercase content and storing them in the directory
        out.write(y)

    if i==99:
        time1 =time.time()-start_time

    elif i==199:
        time2 = time.time()-start_time

    elif i==299:
        time3 =time.time()-start_time

    elif i==399:
        time4 = time.time()-start_time

    elif i==499:
        time5 = time.time()-start_time






x=[100, 200, 300, 400, 500]

y=[time1, time2, time3, time4, time5]

l = [[100,time1],[200,time2], [300,time3], [400,time4] , [500,time5]]
table = tabulate(l, headers=['Number of files', 'Time taken in seconds'], tablefmt='orgtbl')

print(table)


plt.plot(x,y)
plt.xlabel("Number of files")

plt.ylabel("Time taken in seconds")






