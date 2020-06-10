import json 
import csv 
  
  
# Opening JSON file  
with open('data.json') as json_file: 
    data = json.load(json_file) 

# print(type(data))  
  
# now we will open a file for writing 
data_file = open('data_file.csv', 'w') 
  
# create the csv writer object 
csv_writer = csv.writer(data_file) 
  
#    csv_writer.writerow(row)
#    name  ,dept , roll ,mobile , year of admission
#    "userDept" : "ECE",
#    "userMobile" : "7979061755",
#    "userName" : "Nirbhay",
#    "userRoll" : "064",
#    "yearOfAdmission" : "2017"

#print(data['D8x1u9bYMrUJRPQI4I2o7vtJh1V2']['userDept'])
#indices that needs to be charted out
indices = [ 2 ,0 ,3 ,1 ,4]

#headings of each data_point
heading = [ 'NAME' ,'DEPT.' ,'ROLL' , 'MOBILE' , 'YEAR OF ADM.']
csv_writer.writerow(heading)     

#writing the data into the csv file
for i in data:
    data_pts = list(data[i].values())
    new_data_set = []
    #rearranging listed data according to the desired order
    for ind in indices:
        new_data_set.append(data_pts[ind])     
    csv_writer.writerow(new_data_set)


data_file.close() 