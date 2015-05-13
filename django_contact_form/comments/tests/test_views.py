from django.test import TestCase


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

        expected = '<td><input id="name" name="name" type="text" /></td>'
        self.assertContains(response, expected, status_code=200)

        expected = '<td><textarea id="comment" name="comment"></textarea></td>'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="submit" value="Comment!">'
        self.assertContains(response, expected, status_code=200)
