import pandas as pd
import glob
from pathlib import Path
from fpdf import FPDF


def create_pdf_invoice(number: int, date: str, data: pd.DataFrame) -> FPDF:
    pdf = FPDF()
    pdf.set_font(family="Times", style='B', size=12)
    pdf.add_page()
    pdf.cell(txt=f"Invoice nr. {number}", w=0, h=6, ln=1)
    pdf.cell(txt=f"Date {date}", w=0, h=6, ln=1)

    table_structure = {
        'product_id': ['Product ID', 30],
        'product_name': ['Product Name', 60],
        'amount_purchased': ['Amount', 30],
        'price_per_unit': ['Price per Unit', 30],
        'total_price': ['Total Price', 30],
    }

    pdf.ln(4)
    pdf.set_font(family="Times", style='B', size=10)
    for key, params in table_structure.items():
        pdf.cell(txt=params[0], w=params[1], h=8, border=1, ln=0)

    pdf.set_font(family="Times", style='', size=8)
    for index, row in data.iterrows():
        pdf.ln(8)
        for key, params in table_structure.items():
            pdf.cell(txt=str(row[key]), w=params[1], h=8, border=1, ln=0)

    pdf.ln(8)
    total_price = sum(data['total_price'])
    for key, params in table_structure.items():
        text = total_price if key == 'total_price' else ''
        pdf.cell(txt=str(text), w=params[1], h=8, border=1, ln=0)

    pdf.ln(20)
    pdf.set_font(family="Times", style='B', size=10)
    pdf.cell(txt=f"The total due amount is {total_price}", w=0, h=6, ln=1)
    pdf.cell(txt="Leonid Derevianko", w=35, h=6, ln=0)
    pdf.image(name='pypowlogo.png', w=10, h=10, type='png')

    pdf.output('invoice.pdf')
    return pdf


filepaths_list = glob.glob("invoices/*.xlsx")

for filepath in filepaths_list:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    filename = Path(filepath).stem
    invoice_number, invoice_date = filename.split('-')

    pdf_invoice = create_pdf_invoice(invoice_number, invoice_date, df)
    pdf_invoice.output(f"invoices/{filename}.pdf")

