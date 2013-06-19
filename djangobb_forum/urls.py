from django.conf.urls import *

from djangobb_forum import settings as forum_settings
from djangobb_forum import views as forum_views
from djangobb_forum.feeds import LastPosts, LastTopics, LastPostsOnForum, \
     LastPostsOnCategory, LastPostsOnTopic
from djangobb_forum.forms import EssentialsProfileForm, \
    PersonalProfileForm, MessagingProfileForm, PersonalityProfileForm, \
    DisplayProfileForm, PrivacyProfileForm, UploadAvatarForm


urlpatterns = patterns('',

    # Forum
    url('^$', forum_views.index, name='djangobb_index'),
    url('^(?P<forum_id>\d+)/$', forum_views.show_forum, name='djangobb_forum'),
    url('^moderate/(?P<forum_id>\d+)/$', forum_views.moderate, name='djangobb_moderate'),
    url('^search/$', forum_views.search, name='djangobb_search'),
    url('^misc/$', forum_views.misc, name='djangobb_misc'),

    # User
    url('^user/(?P<username>.*)/upload_avatar/$', forum_views.upload_avatar, {
        'form_class': UploadAvatarForm,
        'template': 'djangobb_forum/upload_avatar.html'
        }, name='djangobb_forum_profile_upload_avatar'),
    url('^user/(?P<username>.*)/privacy/$', forum_views.user, {
        'section': 'privacy',
        'form_class': PrivacyProfileForm,
        'template': 'djangobb_forum/profile/profile_privacy.html'
        }, name='djangobb_forum_profile_privacy'),
    url('^user/(?P<username>.*)/display/$', forum_views.user, {
        'section': 'display',
        'form_class': DisplayProfileForm,
        'template': 'djangobb_forum/profile/profile_display.html'
        }, name='djangobb_forum_profile_display'),
    url('^user/(?P<username>.*)/personality/$', forum_views.user, {
        'section': 'personality',
        'form_class': PersonalityProfileForm,
        'template': 'djangobb_forum/profile/profile_personality.html'
        }, name='djangobb_forum_profile_personality'),
    url('^user/(?P<username>.*)/messaging/$', forum_views.user, {
        'section': 'messaging',
        'form_class': MessagingProfileForm,
        'template': 'djangobb_forum/profile/profile_messaging.html'
        }, name='djangobb_forum_profile_messaging'),
    url('^user/(?P<username>.*)/personal/$', forum_views.user, {
        'section': 'personal',
        'form_class': PersonalProfileForm,
        'template': 'djangobb_forum/profile/profile_personal.html'
        }, name='djangobb_forum_profile_personal'),
    url('^user/(?P<username>.*)/essentials/$', forum_views.user, name='djangobb_forum_profile_essentials'),
    url('^user/(?P<username>.*)/$', forum_views.user, name='djangobb_forum_profile'),
    url('^users/$', forum_views.users, name='djangobb_forum_users'),

    # Topic
    url('^topic/(?P<topic_id>\d+)/$', forum_views.show_topic, name='djangobb_topic'),
    url('^(?P<forum_id>\d+)/topic/add/$', forum_views.add_topic, name='djangobb_add_topic'),
    url('^topic/(?P<topic_id>\d+)/delete_posts/$', forum_views.delete_posts, name='djangobb_delete_posts'),
    url('^topic/move/$', forum_views.move_topic, name='djangobb_move_topic'),
    url('^topic/(?P<topic_id>\d+)/stick_unstick/(?P<action>[s|u])/$', forum_views.stick_unstick_topic, name='djangobb_stick_unstick_topic'),
    url('^topic/(?P<topic_id>\d+)/open_close/(?P<action>[c|o])/$', forum_views.open_close_topic, name='djangobb_open_close_topic'),

    # Post
    url('^post/(?P<post_id>\d+)/$', forum_views.show_post, name='djangobb_post'),
    url('^post/(?P<post_id>\d+)/edit/$', forum_views.edit_post, name='djangobb_edit_post'),
    url('^post/(?P<post_id>\d+)/delete/$', forum_views.delete_post, name='djangobb_delete_post'),
    # Post preview
    url(r'^preview/$', forum_views.post_preview, name='djangobb_post_preview'),

    # Subscription
    url('^subscription/topic/(?P<topic_id>\d+)/delete/$', forum_views.delete_subscription, name='djangobb_forum_delete_subscription'),
    url('^subscription/topic/(?P<topic_id>\d+)/add/$', forum_views.add_subscription, name='djangobb_forum_add_subscription'),

    # Feeds
    url(r'^feeds/posts/$', LastPosts(), name='djangobb_forum_posts_feed'),
    url(r'^feeds/topics/$', LastTopics(), name='djangobb_forum_topics_feed'),
    url(r'^feeds/topic/(?P<topic_id>\d+)/$', LastPostsOnTopic(), name='djangobb_forum_topic_feed'),
    url(r'^feeds/forum/(?P<forum_id>\d+)/$', LastPostsOnForum(), name='djangobb_forum_forum_feed'),
    url(r'^feeds/category/(?P<category_id>\d+)/$', LastPostsOnCategory(), name='djangobb_forum_category_feed'),
)

### EXTENSIONS ###

# LOFI Extension
if (forum_settings.LOFI_SUPPORT):
    urlpatterns += patterns('',
        url('^lofi/$', forum_views.index, {'full':False}, name='djangobb_lofi_index'),
        url('^(?P<forum_id>\d+)/lofi/$', forum_views.show_forum, {'full':False}, name='djangobb_lofi_forum'),
        url('^topic/(?P<topic_id>\d+)/lofi/$', forum_views.show_topic, {'full':False}, name='djangobb_lofi_topic'),
    )

# REPUTATION Extension
if (forum_settings.REPUTATION_SUPPORT):
    urlpatterns += patterns('',
        url('^reputation/(?P<username>.*)/$', forum_views.reputation, name='djangobb_reputation'),
    )

# ATTACHMENT Extension
if (forum_settings.ATTACHMENT_SUPPORT):
    urlpatterns += patterns('',
        url('^attachment/(?P<hash>\w+)/$', forum_views.show_attachment, name='djangobb_forum_attachment'),
    )
