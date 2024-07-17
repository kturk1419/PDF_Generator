import pandas as pd
import fpdf as fp
from methods import *


pdf = fp.FPDF(orientation='P', unit="mm", format='A4')
pages = 10
counter = pages

df = pd.read_csv("topics.csv", sep=",")

for i, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(10, 21, 200, 21)



pdf.output("output.pdf")