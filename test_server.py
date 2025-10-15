import unittest
import json
from flaskHttpServer import app 

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_and_list_subscribers(self):
        subscriber_data = {'name': 'Charlie', 'URI': 'http://test.com'}

        add_response = self.app.post('/add-subscriber',
                                     data=json.dumps(subscriber_data),
                                     content_type='application/json')
        
        self.assertEqual(add_response.status_code, 200)

        list_response = self.app.get('/list-subscribers')
        
        self.assertEqual(list_response.status_code, 200)

        data = json.loads(list_response.get_data(as_text=True))
        self.assertIn('Charlie', data)
        self.assertEqual(data['Charlie'], 'http://test.com')

if __name__ == '__main__':
    unittest.main()