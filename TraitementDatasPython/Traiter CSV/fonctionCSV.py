import pandas as pd

def extractCSV(CSVName,listOfColumns,newCSVName):
    """
    Select data we need in a CSV and return an other CSV file
    """
    df = pd.read_csv(CSVName, header=0, delimiter=';')[listOfColumns]
    df.to_csv(newCSVName+".csv", index=False)

if __name__ == '__main__':
    myList = ["date_ech","valeur"]
    extractCSV("indice-qualite-de-lair.csv",myList,"Dataset")