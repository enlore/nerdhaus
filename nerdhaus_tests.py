import os
import app
import unittest
import tempfile


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, app.app.database = tempfile.mkstemp()
        app.app.config['TESTING'] = True 
        self.app = app.app.test_client()
        app.init_db()

    def tearDown(self):
       os.close(self.db_fd)
       os.unlink(app.app.database)

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'no bills' in rv.data

    def test_new_bill(self):
        resp = self.app.get('/new')
        assert resp.status_code == 200
        assert '<form method="post" action="/create_bill">' in resp.data

    def test_create_bill(self):
        data = dict(
                name='Electric Bill',
                pay_to='CDE',
                due_date='2013/4/13',
                due_amount=280.00,
                late_after_date='2013/4/18',
                late_amount=300.00,
                termination_date='2013/4/24'
            )
                
        resp = self.app.post('/create_bill', data=data, follow_redirects=True)

        assert 'Electric Bill' in resp.data
        assert 'CDE' in resp.data
        assert '2013/4/13' in resp.data

    def test_delete_bill(self):
        resp = self.app.get('/delete/1')

        assert 'Electric Bill' not in resp.data
        assert 'CDE' not in resp.data
        assert '2013/4/13' not in resp.data

if __name__ == '__main__':
    unittest.main()
