from glob import glob
from pathlib import Path
from fpdf import FPDF

filepaths_list = glob('files/*.txt')

pdf = FPDF()
pdf.set_auto_page_break(auto=False, margin=0)

for filepath in filepaths_list:
    with open(filepath) as file:
        content = file.read()

    filename = Path(filepath).stem
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(txt=filename.title(), w=20, h=6, ln=1)
    pdf.set_font(family='Times', style='', size=12)
    pdf.multi_cell(txt=content, h=8, w=0)
    # pdf.write(txt=content, h=8)


pdf.output('animals.pdf')

