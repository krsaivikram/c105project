import csv
import math
with open("C:/Users/Manorama/Desktop/data1.csv",newline = "") as f:
    reader = csv.reader(f)
    filedata = list(reader)
    data = filedata[0]
def Mean(data):
    num = len(data)
    total = 0
    for x in data:
        total = total+int(x)
    mean = total/num
    return mean
sqrdlist = []
for number in data:
    a = int(number)-Mean(data)
    a = a**2
    sqrdlist.append(a)
sum = 0
for i in sqrdlist:
    sum = sum+i
result = sum/(len(data)-1)
stddeviation = math.sqrt(result)
print(stddeviation)        
