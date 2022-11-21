from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField
from flatmate_bill import flat

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', bill_form=bill_form)

    def post(self):
        bill_form = BillForm(request.form)
        amount = float(bill_form.amount.data)
        period = bill_form.period.data

        name1 = bill_form.name1.data
        days_in_house1 = float(bill_form.days_in_house1.data)

        name2 = bill_form.name2.data
        days_in_house2 = float(bill_form.days_in_house2.data)

        the_bill = flat.Bill(amount, period)
        flatmate1 = flat.Flatmate(name1, days_in_house1)
        flatmate2 = flat.Flatmate(name2, days_in_house2)

        return render_template("bill_form_page.html",
                               name1=flatmate1.name,
                               name2=flatmate2.name,
                               amount1=flatmate1.pays(the_bill, flatmate2),
                               amount2=flatmate2.pays(the_bill, flatmate1),
                               bill_form=bill_form,
                               result=True,
                               )


# class ResultsPage(MethodView):
#     def post(self):
#         bill_form = BillForm(request.form)
#         amount = float(bill_form.amount.data)
#         period = bill_form.period.data
#
#         name1 = bill_form.name1.data
#         days_in_house1 = float(bill_form.days_in_house1.data)
#
#         name2 = bill_form.name2.data
#         days_in_house2 = float(bill_form.days_in_house2.data)
#
#         the_bill = flat.Bill(amount, period)
#         flatmate1 = flat.Flatmate(name1, days_in_house1)
#         flatmate2 = flat.Flatmate(name2, days_in_house2)
#
#         return render_template("results.html",
#                                name1=flatmate1.name,
#                                name2=flatmate2.name,
#                                amount1=flatmate1.pays(the_bill, flatmate2),
#                                amount2=flatmate2.pays(the_bill, flatmate1)
#                                )


class BillForm(Form):
    amount = StringField("Bill Amount: ", default=0)
    period = StringField("Bill Period: ", default="Month-Year")

    name1 = StringField("Name: ", default="Name1")
    days_in_house1 = StringField("Days in House: ", default=1)

    name2 = StringField("Name: ", default="Name2")
    days_in_house2 = StringField("Days in House: ", default=1)

    submit_button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form/', view_func=BillFormPage.as_view('bill_form_page'))
# app.add_url_rule('/results/', view_func=ResultsPage.as_view('results_page') )

app.run(debug=False)
