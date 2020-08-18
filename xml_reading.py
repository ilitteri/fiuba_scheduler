import pandas as pd
from lxml import etree

def getData(content):
    return [(element.text or '').strip() for element in content.xpath('//span')]

def readHTML(file):
    with open(file, 'r', encoding='utf-8') as xml_file:
        content = etree.parse(xml_file)
        field_count = 11
        reading = getData(content)
        header = reading[:field_count]
        not_header = reading[field_count:]
        data = list(zip(*(not_header[i::field_count] for i in range(field_count))))

    return header, data

def getDataFrame(file):
    header, data = readHTML(file)
    data_frame = pd.DataFrame(data, columns = header)

    return data_frame