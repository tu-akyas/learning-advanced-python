import sqlite3
import uuid
from fpdf import FPDF


class User:
    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        """Buys Ticket if the card is valid"""
        if seat.is_free():
            if card.validate(price=seat.get_price()):
                seat.occupy()
                ticket = Ticket(user=self, price=seat.get_price(), seat_num=seat.seat_id)
                ticket.to_pdf()
                return "Purchase Successful"
            else:
                return "There is a problem with your card details!"
        else:
            return "Seat is not available for booking"


class Seat:
    db = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        connection = sqlite3.connect(Seat.db)
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT "price" FROM "Seat" WHERE "seat_id"=?
            """,
            [self.seat_id]
        )
        result = cursor.fetchall()
        connection.close()
        return result[0][0]

    def is_free(self):
        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT "taken" from "Seat" WHERE "seat_id"=?
            """,
            [self.seat_id]
        )
        result = cursor.fetchall()
        connection.close()

        return result[0][0] == 0

    def occupy(self):
        if self.is_free():
            connection = sqlite3.connect(Seat.db)
            connection.execute(
                """
                UPDATE "Seat" SET "taken"=1 WHERE "seat_id"=?
                """,
                [self.seat_id]
            )
            connection.commit()
            connection.close()


class Card:
    db = 'banking.db'

    def __init__(self, card_type, number, cvv, holder):
        self.type = card_type
        self.number = number
        self.cvv = cvv
        self.holder = holder

    def validate(self, price):
        connection = sqlite3.connect(Card.db)
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT "balance" FROM "Card" WHERE "number"=? AND "cvc"=?
            """,
            [self.number, self.cvv]
        )
        result = cursor.fetchall()
        if result:
            balance = result[0][0]
            if balance >= price:
                connection.execute(
                    """
                    UPDATE "Card" SET "Balance"=? WHERE "number"=? AND "cvc"=?
                    """,
                    [balance - price, self.number, self.cvv]
                )
                connection.commit()
                connection.close()
                return True
            else:
                return False
        else:
            return False


class Ticket:
    def __init__(self, user, price, seat_num):
        self.id = uuid.uuid4()
        self.user = user
        self.price = price
        self.seat_num = seat_num

    def to_pdf(self):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family="Times", style='B', size=24)
        pdf.cell(w=0, h=80, txt="Cinema Ticket", border=1, ln=1, align='c')

        pdf.set_font(family="Times", style='B', size=14)
        pdf.cell(w=100, h=25, txt="Name", border=1)
        pdf.set_font(family="Times", style='', size=12)
        pdf.cell(w=0, h=25, txt=self.user.name, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", style='B', size=14)
        pdf.cell(w=100, h=25, txt="Ticket ID", border=1)
        pdf.set_font(family="Times", style='', size=12)
        pdf.cell(w=0, h=25, txt=str(self.id), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", style='B', size=14)
        pdf.cell(w=100, h=25, txt="Price", border=1)
        pdf.set_font(family="Times", style='', size=12)
        pdf.cell(w=0, h=25, txt=str(self.price), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.output("sample.pdf", 'F')


if __name__ == "__main__":

    name = input("Your Full Name: ")
    seat_id = input("Preferred Seat Number: ")
    card_type = input("your card type: ")
    card_number = input("Your Card Number: ")
    card_cvv = input("Your Card cvv: ")
    card_holder = input("Name of Card Holder: ")

    user = User(name=name)
    seat = Seat(seat_id=seat_id)
    card = Card(card_type=card_type, number=card_number, cvv=card_cvv, holder=card_holder)

    print(user.buy(seat=seat, card=card))