from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase


class TestViews(TestCase):
    fixtures = ('test_forum.json',)

    def test_index(self):
        self.client.get(reverse('djangobb_index'))

    def test_forum(self):
        self.client.get(reverse('djangobb_forum', kwargs={'forum_id': '3'}))

    def test_moderate(self):
        self.client.get(reverse('djangobb_moderate', kwargs={'forum_id': '3'}))

    def test_search(self):
        self.client.get(reverse('djangobb_search'))

    def test_forum_profile_upload_avatar(self):
        self.client.get(reverse('djangobb_forum_profile_upload_avatar', kwargs={'username': 'djangobb'}))

    def test_forum_profile_privacy(self):
        self.client.get(reverse('djangobb_forum_profile_privacy', kwargs={'username': 'djangobb'}))

    def test_forum_profile_display(self):
        self.client.get(reverse('djangobb_forum_profile_display', kwargs={'username': 'djangobb'}))

    def test_forum_profile_personality(self):
        self.client.get(reverse('djangobb_forum_profile_personality', kwargs={'username': 'djangobb'}))

    def test_forum_profile_messaging(self):
        self.client.get(reverse('djangobb_forum_profile_messaging', kwargs={'username': 'djangobb'}))

    def test_forum_profile_personal(self):
        self.client.get(reverse('djangobb_forum_profile_personal', kwargs={'username': 'djangobb'}))

    def test_forum_profile_essentials(self):
        self.client.get(reverse('djangobb_forum_profile_essentials', kwargs={'username': 'djangobb'}))

    def test_forum_profile(self):
        self.client.get(reverse('djangobb_forum_profile', kwargs={'username': 'djangobb'}))

    def test_forum_users(self):
        self.client.get(reverse('djangobb_forum_users'))

    def test_topic(self):
        self.client.get(reverse('djangobb_topic', kwargs={'topic_id': '2'}))

    def test_post(self):
        self.client.get(reverse('djangobb_post', kwargs={'post_id': '1'}))

    def test_forum_posts_feed(self):
        self.client.get(reverse('djangobb_forum_posts_feed'))

    def test_forum_topics_feed(self):
        self.client.get(reverse('djangobb_forum_topics_feed'))

    def test_forum_topic_feed(self):
        self.client.get(reverse('djangobb_forum_topic_feed', kwargs={'topic_id': '2'}))

    def test_forum_forum_feed(self):
        self.client.get(reverse('djangobb_forum_forum_feed', kwargs={'forum_id': '3'}))

    def test_forum_category_feed(self):
        self.client.get(reverse('djangobb_forum_category_feed', kwargs={'category_id': '3'}))

class TestLoginViews(TestCase):
    fixtures = ('test_forum.json',)

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.user.set_password('password')
        self.user.save()
        self.assertTrue(self.client.login(username=self.user.username, password="password"))

    # def test_misc(self):
    #     self.client.get(reverse('djangobb_misc'))

    def test_add_topic(self):
        self.client.get(reverse('djangobb_add_topic', kwargs={'forum_id': '3'}))

    def test_edit_post(self):
        self.client.get(reverse('djangobb_edit_post', kwargs={'post_id': '1'}))

    def test_delete_posts(self):
        self.client.get(reverse('djangobb_delete_posts', kwargs={'topic_id': '2'}))

    # def test_move_topic(self):
    #     self.client.get(reverse('djangobb_move_topic'))

    def test_stick_unstick_topic(self):
        self.client.get(reverse('djangobb_stick_unstick_topic', kwargs={'topic_id': '2', 'action': 's'}))
        self.client.get(reverse('djangobb_stick_unstick_topic', kwargs={'topic_id': '2', 'action': 'u'}))

    def test_delete_post(self):
        self.client.get(reverse('djangobb_delete_post', kwargs={'post_id': '1'}))

    def test_open_close_topic(self):
        self.client.get(reverse('djangobb_open_close_topic', kwargs={'topic_id': '2', 'action': 'o'}))
        self.client.get(reverse('djangobb_open_close_topic', kwargs={'topic_id': '2', 'action': 'c'}))

    def test_forum_delete_subscription(self):
        self.client.get(reverse('djangobb_forum_delete_subscription', kwargs={'topic_id': '2'}))

    def test_forum_add_subscription(self):
        self.client.get(reverse('djangobb_forum_add_subscription', kwargs={'topic_id': '2'}))

    def test_post_preview(self):
        self.client.get(reverse('djangobb_post_preview'))

