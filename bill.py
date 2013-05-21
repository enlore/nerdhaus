class Bill(object):
    def __init__(self, b_id, name, pay_to, due_date, due_amount, late_after_date, late_amount, termination_date):
        self.b_id = b_id
        self.name = name
        self.pay_to = pay_to
        self.due_date = due_date
        self.due_amount = due_amount
        self.late_after_date = late_after_date
        self.late_amount = late_amount
        self.termination_date = termination_date

class BillForm(Form):
    b_id = HiddenField()
    name = TextField(u'Name:', [validators.required()])
    pay_to = TextField(u'Pay To:',[validators.required()])
    due_date = DateField(u'Date Due:',[validators.required()])
    due_amount = DecimalField(u'Amount Due:',places = 2)
    late_after_date = DateField(u'Late After:',[validators.required()])
    late_amount = DecimalField(u'Late Amount:', places = 2)
    termination_date = DateField(u'Termination Date:',[validators.required()])
