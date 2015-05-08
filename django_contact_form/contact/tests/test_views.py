from django.core.urlresolvers import reverse
from django.test import TestCase

from contact.models import Contact


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

        expected = '<td><input id="id_first_name" maxlength="100" '
        expected += 'name="first_name" type="text" /></td>'
        self.assertContains(response, expected, status_code=200)

        expected = '<td>last name:</td>'
        self.assertContains(response, expected, status_code=200)

        expected = '<td><input id="id_last_name" maxlength="100" '
        expected += 'name="last_name" type="text" /></td>'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="submit" value="Submit">'
        self.assertContains(response, expected, status_code=200)

    def test_submit_form_should_have_data_in_database(self):
        self.assertEqual(Contact.objects.all().count(),0)

        data = {
            'first_name': 'Navarat',
            'last_name': 'Pramuksun'
        }
        self.client.post(reverse('contact'),data=data)

        contact = Contact.objects.get(first_name='Navarat')
        self.assertEqual(contact.first_name, 'Navarat')
        self.assertEqual(contact.last_name, 'Pramuksun')

        self.assertEqual(Contact.objects.all().count(),1)
