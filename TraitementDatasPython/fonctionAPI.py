import urllib.request
import json
import csv

def GetRequest(request):
    with urllib.request.urlopen(request) as jsonfile:
        dataJSON = json.loads(jsonfile.read().decode())
        print(dataJSON)
    return(dataJSON)
        
def jsonToCSV(input_json, output_path):
    print("lol")
      
    
if __name__ == '__main__':
    dataJSON = GetRequest("https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=indice-qualite-de-lair&facet=date_ech&facet=valeur")
    #csvfile = open('newFileTest.csv', 'w')
    jsonToCSV(dataJSON, "newFileTest.csv")
