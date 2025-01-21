import csv

with open('TxtItemMaster.csv', 'r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)


data=[["Item100","Item100","Loadsize3"],["Item101","Item101","Loadsize2"]]
with open('TxtItemMaster.csv', 'a', newline='')as file:
    writer= csv.writer(file)
    writer.writerows(data)
