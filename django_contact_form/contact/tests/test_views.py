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
        self.assertEqual(Contact.objects.all().count(), 0)

        data = {
            'first_name': 'Navarat',
            'last_name': 'Pramuksun'
        }
        response = self.client.post(reverse('contact'), data=data, follow=True)

        contact = Contact.objects.get(first_name='Navarat')
        self.assertEqual(contact.first_name, 'Navarat')
        self.assertEqual(contact.last_name, 'Pramuksun')

        self.assertEqual(Contact.objects.all().count(), 1)

        expected = 'Thank you!'
        self.assertContains(response, expected, status_code=200)

        expected = 'First name: Navarat'
        self.assertContains(response, expected, status_code=200)

        expected = 'Last name: Pramuksun'
        self.assertContains(response, expected, status_code=200)


    def test_submit_without_first_name_should_show_error_message(self):
        self.assertEqual(Contact.objects.all().count(), 0)

        data = {
            'first_name': '',
            'last_name': 'Pramuksun'
        }
        response = self.client.post(reverse('contact'), data=data)

        self.assertEqual(Contact.objects.all().count(), 0)

        expected = 'This field is required.'
        self.assertContains(response, expected, status_code=200)

    def test_submit_without_last_name_should_show_error_message(self):
        self.assertEqual(Contact.objects.all().count(), 0)

        data = {
            'first_name': 'Navarat',
            'last_name': ''
        }
        response = self.client.post(reverse('contact'), data=data)

        self.assertEqual(Contact.objects.all().count(), 0)

        expected = 'This field is required.'
        self.assertContains(response, expected, status_code=200)

    def test_submit_without_any_data_should_show_two_error_messages(self):
        self.assertEqual(Contact.objects.all().count(), 0)

        data = {
            'first_name': '',
            'last_name': ''
        }
        response = self.client.post(reverse('contact'), data=data)

        self.assertEqual(Contact.objects.all().count(), 0)

        expected = 'This field is required.'
        self.assertContains(response, expected, count=2, status_code=200)

    def test_submit_form_successfully_should_redirect_to_thank_you_page(self):
        data = {
            'first_name': 'Navarat',
            'last_name': 'Pramuksun'
        }
        response = self.client.post(reverse('contact'), data=data)

        self.assertRedirects(
            response,
            reverse('thank'),
            status_code=302,
            target_status_code=200
        )


class ThankYouViewTest(TestCase):
    def setUp(self):
        Contact.objects.create(
            first_name='lnwBoss',
            last_name='yong'
        )
        self.response = self.client.get(reverse('thank'))

    def test_thank_you_page_should_be_accessible(self):
        self.assertEqual(self.response.status_code, 200)

    def test_thank_you_page_should_display_title_thank_you(self):
        expected = '<h1>Thank you!</h1>'
        self.assertContains(self.response, expected, status_code=200)

    def test_thank_you_page_should_display_latest_first_and_last_name(self):
        expected = 'First name: lnwBoss'
        self.assertContains(self.response, expected, status_code=200)

        expected = 'Last name: yong'
        self.assertContains(self.response, expected, status_code=200)
