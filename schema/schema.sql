DROP TABLE IF EXISTS bills;
CREATE TABLE bills (
    id int PRIMARY KEY AUTO INCREMENT, 
    name text, 
    pay_to text, 
    due_amount real, 
    due_date text, 
    late_amount real, 
    late_after_date real, 
    termination_date text
);

