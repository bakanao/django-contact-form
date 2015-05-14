from django.test import TestCase

from comments.forms import CommentsForm


class CommentsFormTest(TestCase):
    def test_comments_form_should_have_name_and_comment_fields(self):
        expected_fields = ['name', 'comment', 'ip']

        form = CommentsForm()
        for each in expected_fields:
            self.assertTrue(each in form.fields)

        self.assertEqual(len(form.fields), 3)
