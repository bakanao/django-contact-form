from django.db import IntegrityError
from django.test import TestCase

from contact.models import Contact


class ContactTest(TestCase):
    def test_save_contact_successfully(self):
        contact = Contact()
        contact.first_name = 'Navarat'
        contact.last_name = 'Pramuksun'
        contact.email = 'oy@prontomarketing.com'

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

    def test_save_contact_without_first_name_should_fail(self):
        contact = Contact()
        contact.first_name = None
        contact.last_name = 'Pramuksun'
        contact.email = 'oy@prontomarketing.com'

        self.assertRaises(IntegrityError, contact.save)

    def test_save_contact_without_last_name_should_fail(self):
        contact = Contact()
        contact.first_name = 'Navarat'
        contact.last_name = None
        contact.email = 'oy@prontomarketing.com'

        self.assertRaises(IntegrityError, contact.save)

    def test_save_contact_without_email_should_fail(self):
        contact = Contact()
        contact.first_name = 'Navarat'
        contact.last_name = 'Pramuksun'
        contact.email = None

        self.assertRaises(IntegrityError, contact.save)
