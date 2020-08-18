from lxml import html
import pandas as pd
import re

def fixSyntaxError(data, field_count):
    lines = []
    i = 0
    while i < len(data):
        line = []
        field_index = 0
        
        while i < len(data) and field_index < field_count:
            field = data[i]
            if field_index == 5 and re.match(r'^\d\d:\d\d:\d\d$', field) is None:
                #raise Exception('jerston')
                pass

            if field_index == 0 and ' CURSO: ' in field:
                codigo, curso = field.split(' CURSO: ')
                line.extend((codigo, curso))
                field_index += 2
            elif 'CURSO: ' in field:
                line.append(field[field.index(' ') + 1:])
                field_index += 1
            else:
                line.append(field)
                field_index += 1

            i += 1

        lines.append(line)

    return lines

def getHeader(content):
    return [e.encode('latin-1').decode('utf-8') for e in content.xpath('//b/text()')]
    

def getData(content, field_count):
    return [e.getprevious().tail.replace(u'\xa0', ' ').encode('latin-1').decode('utf-8').lstrip('\n') for e in content.xpath('//br')[field_count:]]

def createCSV(data_frame, name_file, header, data ):
    data_frame.to_csv(name_file, index=False, header=True)

def readHTML(file):
    with open(file, 'r', encoding='utf-8') as html_file:
        content = html.parse(html_file)
        header = getHeader(content)
        field_count = len(header)
        data = getData(content, field_count)
        fixed_data = fixSyntaxError(data, field_count)

        #print(jerston)
        #print(d)
        #print(data[::fields])

    return header, fixed_data

def main():
    file = 'html_files/schedules.html'
    header, data  = readHTML(file)
    data_frame = pd.DataFrame(data, columns = header)
    createCSV(data_frame, 'schedule.csv', header, data)

main()