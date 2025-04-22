import csv

f = open("e:\\data11.csv")
csv_data = csv.reader(f)
list1 =list(csv_data)
print(list1)
l =len(list1)
for i in range(0,l):
    print(list1[i][0])
    print(list1[i][1])
    print(list1[i][2])
