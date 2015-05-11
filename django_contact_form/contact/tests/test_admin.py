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

    def test_contact_admin_should_display_first_name_and_last_name(self):
        Contact.objects.create(
            first_name='N',
            last_name='P',
            email='oy@prontomarketing.com'
        )

        response = self.client.get('/admin/contact/contact/')

        expected = '<div class="text"><a href="?o=1">First name</a></div>'
        self.assertContains(response, expected, status_code=200)

        expected = '<div class="text"><a href="?o=2">Last name</a></div>'
        self.assertContains(response, expected, status_code=200)

        expected = '<div class="text"><a href="?o=3">Email</a></div>'
        self.assertContains(response, expected, status_code=200)
