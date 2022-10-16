import csv, json

def gen_obj(row):
    return {
          "value": {
            "bindType": "parameter",
            "binding": "{discordance_ouverture}"
          },
          "valueSource": "opc",
          "opcItemPath": "[S7_1500_Axima_Lacq_2]DB5," + row[6][7:],
          "dataType": "Boolean",
          "alarms": [   
            {
              "name": row[2]
            }
          ],
          "name": row[1],
          "tagType": "AtomicTag",
          "opcServer": "Ignition OPC UA Server"
        }
        
with open(f'c:/Users/XC6362/Documents/HMIAlarms.csv') as csv_file, open('json_data.json', 'w') as json_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    my_json = [gen_obj(row) for row in csv_reader]
    json.dump(my_json, json_file)
  
