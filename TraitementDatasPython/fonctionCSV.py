import pandas as pd

def extractCSV(CSVName,listOfColumns):
    df = pd.read_csv("indice-qualite-de-lair.csv", header=0, delimiter=';')[listOfColumns]
    df.to_csv("newFileTest.csv", index=False)

if __name__ == '__main__':
    myList = ["valeur","type_zone"]
    extractCSV("indice-qualite-de-lair.csv",myList)