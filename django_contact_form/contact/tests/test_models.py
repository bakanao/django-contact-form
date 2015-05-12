from django.db import IntegrityError
from django.test import TestCase

from contact.models import Contact


class ContactTest(TestCase):
    def test_save_contact_successfully(self):
        contact = Contact()
        contact.first_name = 'Navarat'
        contact.last_name = 'Pramuksun'
        contact.email = 'oy@prontomarketing.com'
        contact.ip = '58.137.162.34'
        contact.location = '13.754:100.5014'

        self.assertFalse(contact.id)

        contact.save()

        self.assertTrue(contact.id)

        contact_new = Contact.objects.get(id=contact.id)

        expected = 'Navarat'
        self.assertEqual(contact_new.first_name, expected)

        expected = 'Pramuksun'
        self.assertEqual(contact_new.last_name, expected)

        expected = 'oy@prontomarketing.com'
        self.assertEqual(contact_new.email, expected)

        expected = '58.137.162.34'
        self.assertEqual(contact_new.ip, expected)

        expected = '13.754:100.5014'
        self.assertEqual(contact_new.location, expected)

    def test_save_contact_without_first_name_should_fail(self):
        contact = Contact()
        contact.first_name = None
        contact.last_name = 'Pramuksun'
        contact.email = 'oy@prontomarketing.com'
        contact.ip = '58.137.162.34'
        contact.location = '13.754:100.5014'

        self.assertRaises(IntegrityError, contact.save)

    def test_save_contact_without_last_name_should_fail(self):
        contact = Contact()
        contact.first_name = 'Navarat'
        contact.last_name = None
        contact.email = 'oy@prontomarketing.com'
        contact.ip = '58.137.162.34'
        contact.location = '13.754:100.5014'

        self.assertRaises(IntegrityError, contact.save)

    def test_save_contact_without_email_should_fail(self):
        contact = Contact()
        contact.first_name = 'Navarat'
        contact.last_name = 'Pramuksun'
        contact.email = None
        contact.ip = '58.137.162.34'
        contact.location = '13.754:100.5014'

        self.assertRaises(IntegrityError, contact.save)

    def test_save_contact_without_ip_should_fail(self):
        contact = Contact()
        contact.first_name = 'Navarat'
        contact.last_name = 'Pramuksun'
        contact.email = 'oy@pronto.com'
        contact.ip = None
        contact.location = '13.754:100.5014'

        self.assertRaises(IntegrityError, contact.save)

    def test_save_contact_without_location_should_fail(self):
        contact = Contact()
        contact.first_name = 'Navarat'
        contact.last_name = 'Pramuksun'
        contact.email = 'oy@pronto.com'
        contact.ip = '58.137.162.34'
        contact.location = None

        self.assertRaises(IntegrityError, contact.save)
