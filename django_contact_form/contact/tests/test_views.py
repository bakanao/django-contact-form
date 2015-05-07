from django.core.urlresolvers import reverse
from django.test import TestCase


class ContactViewTest(TestCase):
    def test_contact_page_should_be_accessible(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_should_have_wording_contact_form(self):
        response = self.client.get(reverse('contact'))
        expected = '<h1>Contact Form</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_contact_page_should_have_contact_form(self):
        response = self.client.get(reverse('contact'))

        expected = '<form action="." method="post">'
        self.assertContains(response, expected, status_code=200)

        expected = '<td>first name:</td>'
        self.assertContains(response, expected, status_code=200)

        expected = '<td><input type="text" name="first_name"></td>'
        self.assertContains(response, expected, status_code=200)

        expected = '<td>last name:</td>'
        self.assertContains(response, expected, status_code=200)

        expected = '<td><input type="text" name="last_name"></td>'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="submit" value="Submit">'
        self.assertContains(response, expected, status_code=200)
