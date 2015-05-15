from django.test import TestCase

from comments.models import Comments


class CommentsViewTest(TestCase):
    def test_comments_page_should_be_accessible(self):
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, 200)

    def test_comments_page_should_display_title_comments(self):
        response = self.client.get('/comments/')
        expected = '<h1>Comments</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_comments_page_should_have_comments_form(self):
        response = self.client.get('/comments/')

        expected = '<form action="." method="post">'
        self.assertContains(response, expected, status_code=200)

        expected = '<td><input id="id_name" maxlength="100" name="name" type="text" /></td>'
        self.assertContains(response, expected, status_code=200)

        expected = '<td><textarea cols="40" id="id_comment" name="comment" rows="10">'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="submit" value="Comment!">'
        self.assertContains(response, expected, status_code=200)

    def test_submit_comments_form_should_save_name_and_comment_database(self):
        self.assertEqual(Comments.objects.all().count(), 0)

        data = {
            'name': 'oy',
            'comment': 'hi',
        }
        response = self.client.post('/comments/', data=data)

        comments = Comments.objects.get(name='oy')
        self.assertEqual(comments.name, 'oy')
        self.assertEqual(comments.comment, 'hi')

        self.assertEqual(Comments.objects.all().count(), 1)
