from mock import patch

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

        expected = '<td>email:</td>'
        self.assertContains(response, expected, status_code=200)

        expected = '<td><input id="id_email" name="email" type="email" /></td>'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="submit" value="Submit">'
        self.assertContains(response, expected, status_code=200)

    @patch('contact.views.Geoip')
    def test_submit_form_should_have_data_in_database(self, mock):
        self.assertEqual(Contact.objects.all().count(), 0)

        data = {
            'first_name': 'Navarat',
            'last_name': 'Pramuksun',
            'email': 'oy@prontomarketing.com'
        }
        response = self.client.post(reverse('contact'), data=data, follow=True)

        contact = Contact.objects.get(first_name='Navarat')
        self.assertEqual(contact.first_name, 'Navarat')
        self.assertEqual(contact.last_name, 'Pramuksun')
        self.assertEqual(contact.email, 'oy@prontomarketing.com')

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
            'last_name': '',
            'email': ''
        }
        response = self.client.post(reverse('contact'), data=data)

        self.assertEqual(Contact.objects.all().count(), 0)

        expected = 'This field is required.'
        self.assertContains(response, expected, count=3, status_code=200)

    @patch('contact.views.Geoip')
    def test_submit_form_successfully_should_redirect_to_thank_you_page(
        self,
        mock
    ):
        data = {
            'first_name': 'Navarat',
            'last_name': 'Pramuksun',
            'email': 'oy@prontomarketing.com'
        }
        response = self.client.post(reverse('contact'), data=data)

        self.assertRedirects(
            response,
            reverse('thank'),
            status_code=302,
            target_status_code=200
        )

    @patch('contact.views.Geoip')
    def test_submit_form_successfully_should_call_get_geoip_api(self, mock):
        data = {
            'first_name': 'Navarat',
            'last_name': 'Pramuksun',
            'email': 'oy@prontomarketing.com'
        }
        response = self.client.post(reverse('contact'), data=data)
        mock.return_value.get.assert_called_once_with()

    @patch('contact.views.Geoip')
    def test_submit_form_successfully_should_save_ip_and_location_in_db(
        self,
        mock
    ):
        mock.return_value.get.return_value = {
            u'city': u'Bangkok',
            u'region_code': u'40',
            u'dma_code': u'0',
            u'ip': u'58.137.162.34',
            u'region': u'Krung Thep',
            u'isp': u'CS LOXINFO PUBLIC COMPANY LIMITED',
            u'area_code': u'0',
            u'longitude': 100.5014,
            u'country_code3': u'THA',
            u'continent_code': u'AS',
            u'country_code': u'TH',
            u'offset': u'7',
            u'latitude': 13.754,
            u'timezone': u'Asia/Bangkok',
            u'country': u'Thailand',
            u'asn': u'AS4750'
        }

        data = {
            'first_name': 'Navarat',
            'last_name': 'Pramuksun',
            'email': 'oy@prontomarketing.com'
        }

        response = self.client.post(reverse('contact'), data=data)

        contact = Contact.objects.latest('id')
        self.assertEqual(contact.ip, '58.137.162.34')
        self.assertEqual(contact.location, '13.754:100.5014')


class ThankYouViewTest(TestCase):
    def setUp(self):
        Contact.objects.create(
            first_name='lnwBoss',
            last_name='yong',
            email='boss@pronto.com',
            ip='58.137.162.34',
            location='13.754:100.5014'
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

        expected = 'Email: boss@pronto.com'
        self.assertContains(self.response, expected, status_code=200)

        expected = 'IP: 58.137.162.34'
        self.assertContains(self.response, expected, status_code=200)

        expected = 'Location: 13.754:100.5014'
        self.assertContains(self.response, expected, status_code=200)

    def test_access_thank_you_page_directly_when_no_data_should_show_thank_msg(
        self
    ):
        Contact.objects.all().delete()
        response =  self.client.get(reverse('thank'))

        expected = '<h1>Thank you!</h1>'
        self.assertContains(response, expected, status_code=200)
