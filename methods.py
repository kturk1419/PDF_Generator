import pandas as pd
import fpdf as fp


def add_page(pdf):
    pdf.add_page()
    pdf.set_font(family="Times", size=12)
