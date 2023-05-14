import PyPDF2

pdfFileObj = open('KHPContent.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)

with open('output.txt', 'a') as f:
    for page in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[page]
        text = pageObj.extract_text()
        lines = text.split('\n')

        COPY = False
        for line in range(len(lines)-1):
            sentence = lines[line]
            
            if sentence.startswith('Question'):
                f.write('\n')
                COPY = True
            elif ('(correct)') in sentence: 
                COPY = True
            elif sentence.startswith('Type') or ('Rationale') in sentence: 
                COPY = False
            if(COPY): f.write(sentence + '\n')
                
pdfFileObj.close()






