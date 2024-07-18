import pandas as pd
import fpdf as fp
from methods import *


pdf = fp.FPDF(orientation='P', unit="mm", format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

pages = 10
counter = pages

df = pd.read_csv("topics.csv", sep=",")

for i, row in df.iterrows():
    pdf.add_page()

    pdf.set_font("Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(10, 21, 200, 21)

    # set a footer
    pdf.ln(265)
    pdf.set_font("Times", style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1, border=0)



    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(276)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1, border=0)



pdf.output("output.pdf")