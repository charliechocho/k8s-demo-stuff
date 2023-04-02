import json
import csv

file_csv = 'allmyrecords.csv'

file_json = 'albums.json'

with open(file_csv, 'r') as cfile:
    cdata = csv.reader(cfile, delimiter=';')
    


with open(file_json) as jfile:
    data = json.load(jfile)
    #print(data)
    for item in data:
        print((item['artist']))
        
