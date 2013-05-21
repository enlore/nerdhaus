from wtforms import Form, TextField, DateField, DecimalField, HiddenField, validators
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Bill(Base):
    __tablename__ = 'bills'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    pay_to = Column(String)
    amount_due = Column(Integer)
    date_due = Column(Date)
    amount_late = Column(Integer)
    date_late = Column(Date)
    date_termination = Column(Date)

    def __init__(self, name, pay_to, amount_due, date_due, amount_late, date_late, date_termination):
        self.name               = name
        self.pay_to             = pay_to
        self.amount_due         = amount_due
        self.date_due           = date_due
        self.amount_late        = amount_late
        self.date_late          = date_late
        self.date_termination   = date_termination

    def __repr__(self):
        return "<Bill ('%s', '%s', '%s')>" % (self.name, self.pay_to, self.amount_due)


class BillForm(Form):
    b_id = HiddenField()
    name = TextField(u'Name:', [validators.required()])
    pay_to = TextField(u'Pay To:',[validators.required()])
    due_date = DateField(u'Date Due:',[validators.required()])
    due_amount = DecimalField(u'Amount Due:',places = 2)
    late_after_date = DateField(u'Late After:',[validators.required()])
    late_amount = DecimalField(u'Late Amount:', places = 2)
    termination_date = DateField(u'Termination Date:',[validators.required()])
