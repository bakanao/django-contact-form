from django.contrib.auth.models import User
from django.test import TestCase


class ContactAdminTest(TestCase):
    def test_contact_admin_should_be_accessible(self):
        User.objects.create_superuser(
            'admin',
            'admin@test.com',
            'password'
        )
        self.client.login(username='admin', password='password')
        response = self.client.get('/admin/contact/contact/')
        self.assertEqual(response.status_code, 200)
