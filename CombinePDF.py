import PySimpleGUI as sg
event, values = sg.Window('Combine Multiple PDFs').Layout([[sg.Input(key='_FILES_'), sg.FilesBrowse(file_types=(("PDF Files", "*.pdf"),))], [sg.OK(), sg.Cancel()]]).Read()
print(values['_FILES_'].split(';'))
from pypdf import PdfMerger
pdfs = values['_FILES_'].split(';')


layout =  [[sg.In() ,sg.FileBrowse(file_types=(("Text Files", "*.txt"),))]]

import ntpath
ntpath.basename("a/b/c")
def path_leaf(path):
    return path.strip('/').strip('\\').split('/')[-1].split('\\')[-1]

pdfs=[path_leaf(path) for path in pdfs]
print(pdfs)

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()