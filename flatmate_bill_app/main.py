from flat import Bill, Flatmate
from report import PdfReport

if __name__ == "__main__":

    amount = float(input("Hi! Enter the bill amount: "))
    period = input("Enter the billing period (E.g. Dec 2021): ")

    name1 = input("What is your name? ")
    days_stayed1 = int(input("How many days did you stay in the house during billing period? "))

    name2 = input("Who is sharing the flat with you? Give his/her name: ")
    days_stayed2 = int(input(f"How many days did {name2} stayed during the billing period? "))

    the_bill = Bill(amount, period)
    flatmate1 = Flatmate(name1, days_stayed1)
    flatmate2 = Flatmate(name2, days_stayed2)

    print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, shared_flatmate=flatmate2))
    print(f"{flatmate2.name} pays: ", flatmate2.pays(the_bill, shared_flatmate=flatmate1))

    pdf_report = PdfReport(filename=f"{period} report.pdf")
    pdf_report.generate(flatmate1, flatmate2, the_bill)

