import csv

f=open("e:\\writecs.csv",'w',newline='')
csv_w=csv.writer(f)

csv_w.writerow(['hello',11,12])
csv_w.writerow(['hello1',12,13])
csv_w.writerow(['hello2',13,14])

f.close()