import xml_reading

def createCSV(data_frame, name_file):
    data_frame.to_csv(name_file, index=False, header=True)

def main():
    xml_file = 'schedule.xml'
    df = xml_reading.getDataFrame(xml_file)

    csv_file = f'{xml_file[:xml_file.index(".")]}.csv'
    createCSV(df, csv_file)

main()