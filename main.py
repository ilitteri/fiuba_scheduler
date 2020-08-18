import xml_reading
import csv_creation

def main():
    xml_file = 'schedule.xml'
    df = xml_reading.getDataFrame(xml_file)

    csv_file = f'{xml_file[:xml_file.index(".")]}.csv'
    csv_creation.createCSV(df, csv_file)

main()