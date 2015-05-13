from django.db import IntegrityError
from django.test import TestCase

from comments.models import Comments


class CommentsModelTest(TestCase):
    def test_submit_comment_successfully(self):
        comments = Comments()
        comments.name = 'oy'
        comments.comment = 'hello!'

        self.assertFalse(comments.id)

        comments.save()

        self.assertTrue(comments.id)

        comments_new = Comments.objects.get(id=comments.id)

        expected = 'oy'
        self.assertEqual(comments_new.name, expected)

        expected = 'hello!'
        self.assertEqual(comments_new.comment, expected)

    def test_submit_comment_without_name_should_fail(self):
        comments = Comments()
        comments.name = None
        comments.comment = 'hello!'

        self.assertRaises(IntegrityError, comments.save)

    def test_submit_comment_without_comment_should_fail(self):
        comments = Comments()
        comments.name = 'oy'
        comments.comment = None

        self.assertRaises(IntegrityError, comments.save)
