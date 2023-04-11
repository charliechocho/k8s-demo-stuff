import json
import csv

file_csv = 'allmyrecords/allmyrecords.csv'
file_json = 'allmyrecords/albums.json'

line_list = []
line_list2 = []

with open(file_csv, 'r') as cfile:
    cdata = csv.reader(cfile, delimiter=';')
    for item in cdata:
        line_list.append(item) 
    line_list2.append(line_list[1::217])
    


with open('test.json', 'r') as file:
    jfile = json.load(file)

def load_json(jfile, list):
    # print(len(jfile))
    # print(len(list[0]))
    for i, item in enumerate(list[0]):
        jfile[i]['artist'] = item[0]
        jfile[i]['title'] = item[1]
        jfile[i]['releaseYear'] = item[2]
        jfile[i]['genre'] = item[4]
    
    return jfile

def save_json(file):
    with open('new_albums.json', 'w') as f:
        json.dump(file, f, indent = 2, separators=(',', ': '))




new_jfile = load_json(jfile, line_list2)
save_json(new_jfile)

    # json.dump(line_list2[0][0][0], jfile[0]['artist'])
    # json.dump(line_list2[0][0][1], jfile[0]['title'])
    # json.dump(line_list2[0][0][2], jfile[0]['releaseYear'])
    # json.dump(line_list2[0][0][4], jfile[0]['genre'])
