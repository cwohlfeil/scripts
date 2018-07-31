from PyPDF2 import PdfFileMerger

pdfs = ['Deckblatt_visegrad.pdf', 'visegrad.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('result.pdf', 'wb') as fout:
    merger.write(fout)
