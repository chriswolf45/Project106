import csv 
import numpy as np
def getDataSoucre(data_path):
    Coffeinml = []
    Sleepinhours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffeinml.append(float(row["Coffe in ml"]))
            Sleepinhours.append(float(row["sleep in hours (hours)"]))
    return{"x":Coffeinml,"y":Sleepinhours}
def findCorrelation(dataSoucre):
    correlation = np.corrcoef(dataSoucre["x"],dataSoucre["y"])
    print("correlation is",correlation[0,1])
def setup():
    data_path = "cups of coffe.csv"
    datasoucre = getDataSoucre(data_path)
    findCorrelation(datasoucre)
setup()