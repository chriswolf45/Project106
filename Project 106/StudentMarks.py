import csv 
import numpy as np
def getDataSoucre(data_path):
    Marksinpercentage = []
    Dayspresent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marksinpercentage.append(float(row["Marks In Percentage"]))
            Dayspresent.append(float(row["Days Present(hours)"]))
    return{"x":Marksinpercentage,"y":Dayspresent}
def findCorrelation(dataSoucre):
    correlation = np.corrcoef(dataSoucre["x"],dataSoucre["y"])
    print("correlation is",correlation[0,1])
def setup():
    data_path = "cups of coffe.csv"
    datasoucre = getDataSoucre(data_path)
    findCorrelation(datasoucre)
setup()