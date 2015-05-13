from django.test import TestCase


class CommentsViewTest(TestCase):
    def test_comments_view_should_be_accessible(self):
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, 200)
