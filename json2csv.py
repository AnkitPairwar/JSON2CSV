import json 
import csv 
  
  
# Opening JSON file  
with open('data.json') as json_file: 
    data = json.load(json_file) 
print(type(data))  
  
# now we will open a file for writing 
data_file = open('data_file.csv', 'w') 
  
# create the csv writer object 
csv_writer = csv.writer(data_file) 
  
#csv_writer.writerow(header)
#name  ,dept , roll ,mobile , year of admission
#"userDept" : "ECE",
#    "userMobile" : "7979061755",
#    "userName" : "Nirbhay",
#    "userRoll" : "064",
#    "yearOfAdmission" : "2017"

#print(data['D8x1u9bYMrUJRPQI4I2o7vtJh1V2']['userDept'])
first = list(data.keys())

print(type(first))        
csv_writer.writerow(data[first[0]].keys())       
for i in data:
    csv_writer.writerow(data[i].values())
data_file.close() 