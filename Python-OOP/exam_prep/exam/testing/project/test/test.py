from project.social_media import SocialMedia
import unittest


class TestSocialMedia(unittest.TestCase):
    def setUp(self):
        self.platform1 = SocialMedia("1", "Instagram", 1, "test")

    def test_simple_init(self):
        self.assertEqual(self.platform1._username, "1")
        self.assertEqual(self.platform1._platform, "Instagram")
        self.assertEqual(self.platform1.followers, 1)
        self.assertEqual(self.platform1._content_type, "test")
        self.assertEqual(self.platform1._posts, [])

    def test_platform_setter_only_accepting_valid_type(self):
        self.platform1.platform = "YouTube"
        self.assertEqual(self.platform1.platform, "YouTube")

    def test_platform_setter_raises_error_for_not_valid_type(self):
        with self.assertRaises(ValueError) as ve:
            self.platform1.platform = "should not work"
        self.assertEqual(str(ve.exception),
                         "Platform should be one of ['Instagram', 'YouTube', 'Twitter']")

    def test_followers_setter_with_negative_value_should_result_error(self):
        with self.assertRaises(ValueError) as ve:
            self.platform1.followers = -1
        self.assertEqual(str(ve.exception), "Followers cannot be negative.")

    def test_create_post_method(self):
        result = self.platform1.create_post("test_create_post")
        self.assertEqual(result,
                         "New test post created by 1 on Instagram.")

        self.assertEqual(self.platform1._posts, [{
            'content': "test_create_post", 'likes': 0, 'comments': []}])

    def test_post_with_invalid_index(self):
        self.platform1.create_post("test_post")
        result = self.platform1.like_post(10)
        self.assertEqual(result, "Invalid post index.")

    def test_post_like_with_maximum_number_of_likes(self):
        self.platform1.create_post("test_post")
        self.platform1._posts[0]["likes"] = 10
        result = self.platform1.like_post(0)
        self.assertEqual(result,
                         "Post has reached the maximum number of likes.")

    def test_post_like_works_as_intended(self):
        self.platform1.create_post("test_post")
        result = self.platform1.like_post(0)
        self.assertEqual(result, "Post liked by 1.")
        self.assertEqual(self.platform1._posts[0],
                         {'content': "test_post", 'likes': 1, 'comments': []})

    def test_comment_on_post_with_less_than_10_characters(self):
        self.platform1.create_post("test_post")
        result = self.platform1.comment_on_post(0, "1")
        self.assertEqual(result, "Comment should be more than 10 characters.")

    def test_comment_on_post_with_correct_comment(self):
        self.platform1.create_post("test_post")
        result = self.platform1.comment_on_post(0, "12345678910")
        self.assertEqual(result, "Comment added by 1 on the post.")
        post_comment = self.platform1._posts[0]["comments"][0]
        self.assertEqual(post_comment, {'user': "1", 'comment': "12345678910"})


if __name__ == '__main__':
    unittest.main()
