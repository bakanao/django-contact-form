from django.test import TestCase


class CommentsViewTest(TestCase):
    def test_comments_page_should_be_accessible(self):
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, 200)

    def test_comments_page_should_display_title_comments(self):
        response = self.client.get('/comments/')
        expected = '<h1>Comments</h1>'

        self.assertContains(response, expected, status_code=200)

