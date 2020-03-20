from app import app
from ma import ma
from db import db
from unittest import TestCase


class TestUserResource(TestCase):
    db.init_app(app)
    ma.init_app(app)

    def setUp(self) -> None:
        self.app = app.test_client()

    def test_items_get_list(self):
        response = self.app.get('/items')
        self.assertEqual(response.status_code, 200)