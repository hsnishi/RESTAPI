import requests
import csv

BASE = "http://127.0.0.1:5000/"

def main():
    dev_list = []
    with open("developers.csv", newline='') as csvfile:
        spamreader = csv.reader(csvfile, quotechar=';')
        for row in spamreader:
            data = row[0].split(";")
            dev_list.append({'name':data[0], 'gender': data[1], 'age': (int(data[2])), 'hobby': data[3], 'date_of_birth': data[4]})

    for dev in dev_list:
        response = requests.post(BASE + "developer", data=dev)
        print(response.json())

if __name__ == '__main__':
    main()