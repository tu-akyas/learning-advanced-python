import os
import webbrowser

from fpdf import FPDF
from filestack import Client


class PdfReport:
    """
    Creates a PDF file that contains data of the flatmates and the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, shared_flatmate=flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, shared_flatmate=flatmate1), 2))

        pdf = FPDF(orientation='p', unit='pt', format='A4')
        pdf.add_page()

        # Add house.png icon
        pdf.image("files/house.png", w=50, h=50)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align='c', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period: ", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of Second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        # change directory to files, then generate and open PDF
        os.chdir('files/')
        pdf.output(self.filename)
        webbrowser.open('file://' + os.path.realpath(self.filename))


class FileSharer:

    def __init__(self, filepath, api_key="GET YOUR OWN API KEY"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url
