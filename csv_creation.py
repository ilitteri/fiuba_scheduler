import re
import pdfplumber
from collections import namedtuple

days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

#line_re = r'(\d{4}) CURSO: (\d{1,2}\w?)'

'''def getDay(days, line):
    i = 0
    while i < len(days) and not days[i] in line:
        i += 1
    return -1 if i == len(days) else days[i]'''

subjectCode_re = r'(\d{4})\s'
course_re = r'CURSO:\s(\d{1,2}\D?)'
time_re = r'\d{2}:\d{2}:\d{2}'
classType_re = r'\d{2}:\d{2}:\d{2}\s(\D{1,3})\s'
classroom_re = r'\s(\d{3})\s'
vacancies_re = r'\d{2}:\d{2}:\d{2}\s\D{1,3}\s([3-9][0-9])\s'
day_re = r'\s(Lunes|Martes|Miércoles|Jueves|Viernes)\s'
professor_re = r'\s([A-Z|Ñ]+,\s[A-Z|Ñ]+)\s'
subject_re = r'CURSO:\s\d{1,2}\D?\s([A-Z|\s|.]+)\s[A-Z|Ñ]+,\s[A-Z|Ñ]+\s'
#location_re = r'\s(\D{2})'

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
                print(re.findall(subject_re, line))
            

def main():
    file = 'schedule.pdf'
    read_pdf(file)

main()