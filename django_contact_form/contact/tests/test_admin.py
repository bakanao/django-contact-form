from django.contrib.auth.models import User
from django.test import TestCase

from contact.models import Contact


class ContactAdminTest(TestCase):
    def setUp(self):
        User.objects.create_superuser(
            'admin',
            'admin@test.com',
            'password'
        )
        self.client.login(username='admin', password='password')

    def test_contact_admin_should_be_accessible(self):
        response = self.client.get('/admin/contact/contact/')
        self.assertEqual(response.status_code, 200)

    def test_contact_admin_should_display_all_fields_in_columns(self):
        Contact.objects.create(
            first_name='N',
            last_name='P',
            email='oy@prontomarketing.com',
            ip='58.137.162.34',
            lat = '13.754',
            lng = '100.5014'
        )

        response = self.client.get('/admin/contact/contact/')

        expected = '<div class="text"><a href="?o=1">First name</a></div>'
        self.assertContains(response, expected, status_code=200)

        expected = '<div class="text"><a href="?o=2">Last name</a></div>'
        self.assertContains(response, expected, status_code=200)

        expected = '<div class="text"><a href="?o=3">Email</a></div>'
        self.assertContains(response, expected, status_code=200)

        expected = '<div class="text"><a href="?o=4">Ip</a></div>'
        self.assertContains(response, expected, status_code=200)

        expected = '<div class="text"><a href="?o=5">Lat</a></div>'
        self.assertContains(response, expected, status_code=200)

        expected = '<div class="text"><a href="?o=6">Lng</a></div>'
        self.assertContains(response, expected, status_code=200)

    def test_contact_admin_should_have_search_box_by_email(self):
        Contact.objects.create(
            first_name='Navarat',
            last_name='P',
            email='oy@prontomarketing.com'
        )

        response = self.client.get('/admin/contact/contact/?q=pronto')

        expected = 'Navarat'
        self.assertContains(response, expected, status_code=200)
