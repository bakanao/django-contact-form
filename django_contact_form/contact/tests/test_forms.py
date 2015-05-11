from django import forms
from django.test import TestCase

from contact.forms import ContactForm


class ContactFormTest(TestCase):
    def test_contact_form_should_have_first_name_and_last_name_fields(self):
        expected_fields = ['first_name','last_name', 'email']

        form = ContactForm()
        for each in expected_fields:
            self.assertTrue(each in form.fields)

        self.assertEqual(len(form.fields), 3)

    def test_contact_form_with_valid_data_should_be_valid_and_have_no_errors(
        self
    ):
        valid_data = {
            'first_name': 'N',
            'last_name': 'P',
            'email': 'oy@prontomarketing.com'
        }

        form = ContactForm(data=valid_data)

        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)

    def test_contact_form_with_invalid_data_should_be_invalid_and_have_errors(
        self
    ):
        invalid_data = [
            {
                'first_name': '',
                'last_name': 'P',
                'email': 'oy@prontomarketing.com'
            },
            {
                'first_name': 'N',
                'last_name': '',
                'email': 'oy@prontomarketing.com'
            },
            {
                'first_name': '',
                'last_name': '',
                'email': 'oy@prontomarketing.com'
            },
            {
                'first_name': '',
                'last_name': '',
                'email': ''
            }
        ]

        for each in invalid_data:
            form = ContactForm(data=each)

            self.assertFalse(form.is_valid())
            self.assertTrue(form.errors)

    def test_email_field_should_use_email_widget(self):
        form = ContactForm()

        self.assertIsInstance(form.fields['email'].widget, forms.EmailInput)
