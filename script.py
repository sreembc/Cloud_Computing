import os
import socket
hostname = socket.gethostname()
MyIP = socket.gethostbyname(hostname)
 

file1 = "/home/data/IF.txt"
file2 = "/home/data/Limerick-1.txt"
 
f1 = open(file1)
f2 = open(file2)
lines1 = f1.readlines()
f1.close()

lines2 = f2.readlines()
f2.close()

#os.mkdir(path='/home/output', mode=777)

result_file = open("/home/output/result.txt", "w+") 

path = "/home/data/"
dir_list = os.listdir(path)
result_file.write("List of all the text files at location: /home/data:\n")
for i in dir_list:
    if ".txt" in i:
        result_file.write(i + " \t")
sum1 = 0
sum2 = 0
dict1 = {}
for l in lines1:
  if l != "\n":
    x = l.split(" ")
    sum1 += len(x)
    for w in x:
        if w not in dict1:
            dict1[w] = 1
        else:
            dict1[w] += 1
    

for l in lines2:
  sum2 += len(l.split(" "))

o1 = "\nWord count in IF.txt : " + str(sum1) + "\n"
o2 = "Word count in Limerick-1.txt : " + str(sum2)+ "\n"
o3 = "Total Word count :" + str(sum1+sum2)+ "\n"

result_file.write(o1)
result_file.write(o2)
result_file.write(o3)

sorted_count = sorted(dict1.items(), key=lambda x:x[1], reverse=True)
result_file.write("Top 3 words with maximum number of counts in IF.txt -\n")

a = 1
for i in sorted_count:
    if a <= 3:
        o4 = str(i[0])+" : "+str(i[1])+ "\n"
        a += 1
        result_file.write(o4)
        

result_file.write("IP Address of this machine is: " + MyIP)
result_file.close()

f3 = open("/home/output/result.txt")
lines3 = f3.readlines()
result_file.close()

for line in lines3:
    print(line)

