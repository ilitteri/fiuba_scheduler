import pdfplumber

def read_pdf(file):
    trans = str.maketrans('áéíóúäëïöüÁÉÍÓÚÄËÏÖÜ', 'aeiouaeiouAEIOUAEIOU')
    with pdfplumber.open(file) as pdf, open('schedule.csv', 'w') as csv:
        pages = pdf.pages
        first_line = True
        for page in pages:
            text = page.extract_text().translate(trans)
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

main()
'''
trans = str.maketrans('áéíóúäëïöüÁÉÍÓÚÄËÏÖÜ', 'aeiouaeiouAEIOUAEIOU')
with pdfplumber.open('schedule.pdf') as pdf, open('schedule.txt', 'w') as out:
    pages = pdf.pages
    first_line = True
    for page in pages:
        text = page.extract_text().translate(trans)
        out.write(text)
        break
'''