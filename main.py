from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')

df = pd.read_csv("topics.csv")

for idx, row in df.iterrows():
    if idx != 0:
        topic = row["Topic"]
        pages = row["Pages"]
        pdf.add_page()
        pdf.set_font("Arial", size=24, style='B')
        pdf.cell(0, 24, txt=topic, ln=True, align='L', border='B')
        for i in range(pages-1):
            pdf.add_page()

pdf.output("output.pdf")
