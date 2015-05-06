from django.test import TestCase
class ContactViewTest(TestCase):
    def test_contact_page_should_be_accessible(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
