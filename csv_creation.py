import re
import pdfplumber
from collections import namedtuple

#days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']


'''def getDay(days, line):
    i = 0
    while i < len(days) and not days[i] in line:
        i += 1
    return -1 if i == len(days) else days[i]'''

#line_re = r'(\d{4}) CURSO: (\d{1,2}\D?) ([A-Z| |.]+) ([A-Z|Ñ]+, [A-Z|Ñ]+) (Lunes|Martes|Miércoles|Jueves|Viernes) (\d{2}:\d{2}:\d{2}) (\d{2}:\d{2}:\d{2}) (\D{1,3}) (\d{1,2}) (\d{3})'
line_re = r'(\d{4}) CURSO: (\d{1,2}\D?) ([A-Z .]+) ([A-ZÑ]{3,}(?: [A-ZÑ])* +, [A-ZÑ]+) '

subjectCode_re = r'(\d{4}) '
course_re = r'CURSO: (\d{1,2}\D?)'
subject_re = r'CURSO: \d{1,2}\D? ([A-Z| |.]+) [A-Z|Ñ]+, [A-Z|Ñ]+ '
professor_re = r' ([A-Z|Ñ]+, [A-Z|Ñ]+) '
day_re = r' (Lunes|Martes|Miércoles|Jueves|Viernes) '
time_re = r'(\d{2}:\d{2}:\d{2})'
classType_re = r'\d{2}:\d{2}:\d{2} (\D{1,3}) '
vacancies_re = r'\d{2}:\d{2}:\d{2} \D{1,3} (\d{1,2}) ' #
classroom_re = r' (\d{3}) '
#location_re = r' (\D{2})'

def read_pdf(file):
    with pdfplumber.open(file) as pdf, open('schedule.csv', 'w') as csv:
        pages = pdf.pages
        first_line = True
        for page in pages:
            text = page.extract_text()
            for line in text.split('\n'):
                if first_line:
                    #analyzeFirstLine(line)
                    first_line = False
                #print(getDay(days, line))
                print(re.findall(line_re, line))
            break

def main():
    file = 'schedule.pdf'
    read_pdf(file)

#main()
with pdfplumber.open('schedule.pdf') as pdf, open('schedule.txt', 'w') as out:
    pages = pdf.pages
    first_line = True
    for page in pages:
        text = page.extract_text()
        out.write(text)
