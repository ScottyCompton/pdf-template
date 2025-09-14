import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)


df = pd.read_csv("topics.csv")

for idx, row in df.iterrows():
    if idx != 0:
        topic = row["Topic"]
        pages = row["Pages"]
        pdf.add_page()
        pdf.set_font("Times", size=24, style="B")
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 12, txt=topic, ln=True, align="L")
        pdf.line(10, 21, 200, 21)

        pdf.ln(267)  # Move to the bottom of the page
        pdf.set_font("Times", size=8, style="I")
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 10, txt=topic, align="R")

        for i in range(21, 300, 10):
            pdf.ln(i)
            pdf.line(10, i, 200, i)

        for i in range(pages - 1):
            pdf.add_page()
            pdf.ln(278)  # Move to the bottom of the page
            pdf.set_font("Times", size=8, style="I")
            pdf.set_text_color(180, 180, 180)
            pdf.cell(0, 10, txt=topic, align="R")

            for i in range(21, 300, 10):
                pdf.ln(i)
                pdf.line(10, i, 200, i)

pdf.output("output.pdf")
