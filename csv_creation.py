import re
import pdfplumber
from collections import namedtuple

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
                print(re.findall(time_re, line))
                #csv.write(','.join(line.split()) + '\n')

def main():
    file = 'schedule.pdf'
    read_pdf(file)

main()