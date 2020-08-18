import pandas as pd

def createCSV(data_frame, name_file):
    data_frame.to_csv(name_file, index=False, header=True)