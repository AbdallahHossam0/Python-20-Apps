import glob
from pathlib import Path

import pandas as pd
from fpdf import FPDF


def create_invoice_pdf(filepath):
    # Get the Invoice number and date from the filename
    file_name = Path(filepath).stem
    invoice_number, invoice_date = file_name.split("-")

    # Create a PDF instance
    pdf = FPDF("p", "mm", "A4")
    pdf.add_page()

    # Add Invoice number and date to the PDF
    pdf.set_font("Times", "B", 16)
    pdf.cell(w=0, h=6, txt=f"Invoice #: {invoice_number}", ln=True)
    pdf.cell(w=0, h=6, txt=f"Date: {invoice_date}", ln=True)
    pdf.ln(5)

    # Read the invoice data
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Reformat the invoice headers
    headers = [header.replace("_", " ").title() for header in df.columns]

    # Add the invoice headers to the PDF
    pdf.set_font("Times", "B", 10)
    sizes = [30, 70, 33, 30, 30]
    for header, size in zip(headers, sizes):
        pdf.cell(w=size, h=10, txt=header, border=True)
    pdf.ln()

    # Add the items of the invoice to the PDF
    pdf.set_font("Times", size=10)
    for _, row_elements in df.iterrows():
        for row_element, size in zip(row_elements, sizes):
            pdf.cell(w=size, h=10, txt=str(row_element), border=True)
        pdf.ln()

    # Add the total amount to the table
    total_sum = df["total_price"].sum()
    pdf.set_font("Times", "B", 16)
    pdf.cell(w=sum(sizes) - sizes[-1], h=10, txt="Total Amount: ", border=True)
    pdf.cell(w=sizes[-1], h=10, txt=str(total_sum), border=True, ln=True)
    pdf.ln(1)

    # Add the total amount after the table
    pdf.set_font("Times", "B", 16)
    pdf.cell(w=0, h=12, txt=f"The total amount: {total_sum} EGP", border=False, ln=True)

    # Output the PDF file to the disk
    pdf.output(f"PDFs/{file_name}.pdf")


# Loop through all available invoices
for filepath in glob.glob("Invoices/*.xlsx"):
    create_invoice_pdf(filepath)
