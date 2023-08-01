from django.test import TestCase


class BookViewSetTestCase(TestCase):

    def test_book_list_no_authentication(self):
        response = self.client.get('/books/')
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 0

class AuthorsViewSetTestCase(TestCase):

    def test_book_list_no_authentication(self):
        response = self.client.get('/books/')
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 0