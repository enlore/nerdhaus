import os
import app
import unittest
import tempfile


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, nerdhaus.app.database = tempfile.mkstemp()
        nerdhaus.app.config['TESTING'] = True 
        self.app = nerdhaus.app.test_client()
        app.init_db()

    def tearDown(self):
       os.close(self.db_fd)
       os.unlink(nerdhaus.app.database)

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'no bills' in rv.data

    def test_create_bill(self):
        rv = self.app.post('/create_bill', 
            data = dict(
                name='Electric Bill',
                pay_to='CDE',
                due_date='2013/4/13',
                due_amount=280.00,
                late_after_date='2013/4/18',
                late_after_amount=300.00,
                termination_date='2013/4/24'
        ), follow_redirects = True)

        print rv.data

        assert 'Electric Bill' in rv.data
        assert 'CDE' in rv.data
        assert '2013/4/13' in rv.data

if __name__ == '__main__':
    unittest.main()
