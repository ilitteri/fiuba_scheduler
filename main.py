import xml_reading
import csv_creation

def main():
    file = 'schedule.xml'
    data_frame = xml_reading.getDataFrame(file)
    csv_creation.createCSV(data_frame, f'{file[:file.index(".")]}.csv')

main()