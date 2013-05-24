from wtforms import Form, TextField, DateField, IntegerField, HiddenField, validators
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

    # @param parties integer number of people splitting the bill
    def calculate_split(self, parties):
        return self.amount_due / parties 

    def __init__(self, name, pay_to, amount_due, date_due, amount_late, date_late, date_termination):
        self.name               = name
        self.pay_to             = pay_to
        self.amount_due         = amount_due
        self.date_due           = date_due
        self.amount_late        = amount_late
        self.date_late          = date_late
        self.date_termination   = date_termination

    def __repr__(self):
        return "<Bill ('%s', '%s', '%s', '%s')>" % (self.name, self.pay_to, self.amount_due, self.date_due)


class BillForm(Form):
    id                  = HiddenField()
    name                = TextField(u'Name:', [validators.required()])
    pay_to              = TextField(u'Pay To:',[validators.required()])
    date_due            = DateField(u'Date Due:',[validators.required()])
    amount_due          = IntegerField(u'Amount Due:', [validators.required()])
    date_late           = DateField(u'Late After:',[validators.required()])
    amount_late         = IntegerField(u'Late Amount:', [validators.required()])
    date_termination    = DateField(u'Termination Date:',[validators.required()])
