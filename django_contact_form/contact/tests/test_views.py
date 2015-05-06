from django.test import TestCase
class ContactViewTest(TestCase):
    def test_contact_page_should_be_accessible(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_should_have_wording_contact_form(self):
        response = self.client.get('/contact/')
        expected = '<h1>Contact Form</h1>'
        self.assertContains(response, expected, status_code=200)
