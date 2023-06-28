from typing import Iterable
from fpdf import FPDF
import pandas as pd
from pandas import Series


def add_pdf_page(pdf: FPDF, row_data: Series):
    title = row_data['Topic']
    number_of_pages = int(row_data['Pages'])
    number_of_pages = 1
    print(title)
    for page in range(number_of_pages):
        pdf.add_page()
        pdf.set_font(family='Times', style="B", size=12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=f'{title}', align='L', ln=1)
        pdf.line(10, 20, 200, 20)

        pdf.ln(263)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=f'{title} {pdf.page_no()}', align='R', ln=1)

    return pdf


main_pdf = FPDF(orientation='P', unit='mm', format='A4')
main_pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    main_pdf = add_pdf_page(main_pdf, row)

main_pdf.output('output.pdf')

