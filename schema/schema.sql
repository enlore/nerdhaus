DROP TABLE IF EXISTS bills;
CREATE TABLE bills (
    bill_id integer PRIMARY KEY AUTOINCREMENT, 
    name text, 
    pay_to text, 
    due_amount real, 
    due_date text, 
    late_amount real, 
    late_after_date real, 
    termination_date text
);

