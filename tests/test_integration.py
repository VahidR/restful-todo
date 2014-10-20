import re
import threading
import unittest
from selenium import webdriver
from app import create_app, db
from app.models import Todo


class IntegrationTestCase(unittest.TestCase):
    client = None

    @classmethod
    def setUpClass(cls):
        # start Firefox
        try:
            cls.client = webdriver.Firefox()
        except:
            pass

        if cls.client:
            cls.app = create_app('testing')
            cls.app_context = cls.app.app_context()
            cls.app_context.push()


            db.drop_all()
            db.create_all()
            todo = Todo(title='title1', body='body1')
            db.session.add(todo)
            db.session.commit()


            threading.Thread(target=cls.app.run).start()

    @classmethod
    def tearDownClass(cls):
        if cls.client:
            cls.client.close()

            db.drop_all()
            db.session.remove()

            cls.app_context.pop()

    def setUp(self):
        if not self.client:
            self.skipTest('Web browser not available')

    def tearDown(self):
        pass


    def test_home_page(self):
        self.client.get('http://localhost:5000/')
        self.assertTrue(re.search('RESTful', self.client.page_source))

    def test_new_page(self):
        self.client.get('http://localhost:5000/')
        self.client.find_element_by_link_text('New Todo').click()
        self.assertTrue('Back to list' in self.client.page_source)
        self.client.find_element_by_name('title').send_keys('SelTitle')
        self.client.find_element_by_name('body').send_keys('selenium body')
        self.client.find_element_by_name('submit').click()
        self.assertTrue(re.search('SelTitle', self.client.page_source))
