from flask.helpers import url_for
from flask_testing import TestCase
from flask import current_app
from main import app

class MainTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app


    def test_app_exists(self):
        self.assertIsNotNone(current_app)


    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])


    def test_index_redirects(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('login'))

    
    def test_login_get(self):
        response = self.client.get(url_for('login'))
        self.assert200(response)

    
    def test_login_post(self):
        fake_form = {
            'username': 'esteban',
            'password': '12345'
        }
        response = self.client.post(url_for('login'), data=fake_form)
        self.assertRedirects(response, url_for('home'))
