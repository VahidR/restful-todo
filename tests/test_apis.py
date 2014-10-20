import unittest
from flask import url_for
from app import create_app, db
from app.models import Todo

class TestAPIs(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def get_username(self, username):
        if username == 'test':
            password = 'test'
            return True
        return None

    def test_404(self):
        response = self.client.get('/some-wrong/url')
        self.assertTrue(response.status_code == 404)

    def test_no_auth(self):
        response = self.client.get('/todos/api/v1.0/todos',
                                   content_type='application/json')
        self.assertTrue(response.status_code == 403)
